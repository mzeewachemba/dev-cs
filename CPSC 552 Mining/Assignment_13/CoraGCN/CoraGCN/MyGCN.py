from torch_geometric.nn import GCNConv
import torch.nn.functional as F
from torch import nn
import torch


class MyGCN(nn.Module):
    """
    A custom GCN (Graph Convolutional Network) model with two GCN layers.

    This class defines a GCN model with two GCNConv layers followed by a linear layer for classification.

    Args:
        num_features (int): The number of input features per node.
        num_hidden (int): The number of hidden features in the second GCNConv layer.
        num_classes (int): The number of output classes.
    """

    def __init__(self, num_features, num_hidden, num_classes):
        super().__init__()
        torch.manual_seed(1234567)
        self.conv1 = GCNConv(num_features, 50)
        self.conv2 = GCNConv(50, num_hidden)
        self.linearnet = nn.Linear(num_hidden, num_classes)

    def forward(self, x, edge_index):
        """
        Performs the forward pass of the GCN model with two GCN layers.

        Args:
            x (torch.Tensor): The input node features.
            edge_index (torch.Tensor): The edge indices representing the graph structure.

        Returns:
            tuple: A tuple containing the hidden representation (h) and the output logits.
        """

        o1 = self.conv1(x, edge_index)
        o2 = F.relu(o1)  # Apply ReLU activation
        o3 = F.dropout(o2, p=0.5, training=self.training)  # Dropout only during training
        h = self.conv2(o3, edge_index)
        out = self.linearnet(h)
        return out, h
