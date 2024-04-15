import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.nn.init as init
from MSELoss_with_Mask import MSELoss_with_Mask


def activation(input, type):
    """
    Applies activation function based on the provided type.

    Args:
        input (torch.Tensor): Input tensor.
        type (str): Type of activation function (e.g., 'selu', 'relu').

    Returns:
        torch.Tensor: The input tensor after applying the activation function.
    """

    if type.lower() == 'selu':
        return F.selu(input)
    elif type.lower() == 'elu':
        return F.elu(input)
    elif type.lower() == 'relu':
        return F.relu(input)
    elif type.lower() == 'relu6':
        return F.relu6(input)
    elif type.lower() == 'lrelu':
        return F.leaky_relu(input)
    elif type.lower() == 'tanh':
        return F.tanh(input)
    elif type.lower() == 'sigmoid':
        return F.sigmoid(input)
    elif type.lower() == 'swish':
        return F.sigmoid(input) * input
    elif type.lower() == 'identity':
        return input
    else:
        raise ValueError("Unknown non-Linearity Type")


class AutoEncoder(nn.Module):
    def __init__(self, layer_sizes, nl_type='selu', is_constrained=True,
                 dp_drop_prob=0.0, last_layer_activations=True):
        """
        Initializes an AutoEncoder model.

        Args:
            layer_sizes (list): List of integers representing the size of each layer in the model.
                For example, [10000, 1024, 512] will result in an encoder with 2 layers and a decoder
                with 2 layers.
            nl_type (str, optional): Type of non-linearity activation function (default: 'selu').
            is_constrained (bool, optional): If True, encoder and decoder weights are tied. Defaults to True.
            dp_drop_prob (float, optional): Dropout probability for regularization (default: 0.0).
            last_layer_activations (bool, optional): Whether to apply activation on the last decoder layer
                (default: True).
        """

        super(AutoEncoder, self).__init__()
        self.layer_sizes = layer_sizes
        self.nl_type = nl_type
        self.is_constrained = is_constrained
        self.dp_drop_prob = dp_drop_prob
        self.last_layer_activations = last_layer_activations

        if dp_drop_prob > 0:
            self.drop = nn.Dropout(dp_drop_prob)

        self._last = len(layer_sizes) - 2  # Index of the last layer for encoder (excluding bottleneck)

        # Initialize encoder weights with Xavier uniform initialization
        self.encoder_weights = nn.ParameterList(
            [nn.Parameter(torch.rand(layer_sizes[i + 1], layer_sizes[i])) for i in
             range(len(layer_sizes) - 1)]
        )
        for weights in self.encoder_weights:
            init.xavier_uniform_(weights)

        # Initialize encoder bias terms
        self.encoder_bias = nn.ParameterList(
            [nn.Parameter(torch.zeros(layer_sizes[i + 1])) for i in range(len(layer_sizes) - 1)]
        )

        # Define decoder layers (weights are tied or created separately based on is_constrained)
        reverse_layer_sizes = list(reversed(layer_sizes))
        if is_constrained == False:
            self.decoder_weights = nn.ParameterList(
                [nn.Parameter(torch.rand(reverse_layer_sizes[i + 1], reverse_layer_sizes[i])) for i in
                 range(len(reverse_layer_sizes) - 1)]
            )
            for weights in self.decoder_weights:
                init.xavier_uniform_(weights)
            self.decoder_bias = nn.ParameterList(
                [nn.Parameter(torch.zeros(layer_sizes[i+1])) for i in range(len(layer_sizes) - 1) ])
                
            reverse_layer_sizes = list(reversed(layer_sizes))
            # reversed returns iterator
            # Decoder Weights
            if is_constrained == False:
                self.decoder_weights = nn.ParameterList(
                    [nn.Parameter(torch.rand(reverse_layer_sizes[i + 1], reverse_layer_sizes[i])) for i in
                     range(len(reverse_layer_sizes) - 1)]
                )
                for weights in self.decoder_weights:
                    init.xavier_uniform_(weights)
                self.decoder_bias = nn.ParameterList(
                    [nn.Parameter(torch.zeros(reverse_layer_sizes[i + 1])) for i in
                     range(len(reverse_layer_sizes) - 1)])
    
    def encode(self, x):
        """
        Encodes the input data through the encoder layers.

        Args:
            x (torch.Tensor): The input tensor.

        Returns:
            torch.Tensor: The encoded representation of the input.
        """
        for i, w in enumerate(self.encoder_weights):
            x = F.linear(input=x, weight=w, bias=self.encoder_bias[i])
            x = activation(input=x, type=self.nl_type)
        # Apply Dropout on the last layer
        if self.dp_drop_prob > 0:
            x = self.drop(x)
        return x

    # def decode(self, x):
    #     """
    #     Decodes the encoded representation through the decoder layers.

    #     Args:
    #         x (torch.Tensor): The encoded representation.

    #     Returns:
    #         torch.Tensor: The reconstructed output.
    #     """
    #     if self.is_constrained == True:
    #         # Weights are tied
    #         for i, w in zip(range(len(self.encoder_weights)), list(reversed(self.encoder_weights))):
    #             x = F.linear(input=x, weight=w.t(), bias=self.decoder_bias[i])
    #             x = activation(input=x, type=self.nl_type if i != self._last or self.last_layer_activations else 'identity')
    #     else:
    #         for i, w in enumerate(self.decoder_weights):
    #             x = F.linear(input=x, weight=w, bias=self.decoder_weights[i])
    #             x = activation(input=x, type=self.nl_type if i != self._last or self.last_layer_activations else 'identity')
    #     return x


    def decode(self, x):
        """
        Decodes the encoded representation through the decoder layers.

        Args:
            x (torch.Tensor): The encoded representation.

        Returns:
            torch.Tensor: The reconstructed output.
        """
        if self.is_constrained == True:
            # Weights are tied
            for i, w in zip(range(len(self.encoder_weights)), list(reversed(self.encoder_weights))):
                x = F.linear(input=x, weight=w.t(), bias=self.encoder_bias[i])
                x = activation(input=x, type=self.nl_type if i != self._last or self.last_layer_activations else 'identity')
        else:
            for i, w in enumerate(self.decoder_weights):
                x = F.linear(input=x, weight=w, bias=self.decoder_bias[i])
                x = activation(input=x, type=self.nl_type if i != self._last or self.last_layer_activations else 'identity')
        return x

    def forward(self, x):
        """
        Performs the complete forward pass of the autoencoder.

        Args:
            x (torch.Tensor): The input tensor.

        Returns:
            torch.Tensor: The reconstructed output.
        """
        # Forward Pass
        return self.decode(self.encode(x))


 
      
