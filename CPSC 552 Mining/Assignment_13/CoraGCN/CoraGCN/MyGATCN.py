from torch_geometric.nn import GATConv
from torch import nn
import torch
import torch.nn.functional as F


class MyGATCN(nn.Module):
    """
    A custom GAT (Graph Attention Network) model with two GATConv layers.

    This class defines a GAT model with two GATConv layers with multiple attention heads, followed by a linear layer for classification.

    Args:
        num_features (int): The number of input features per node.
        num_hidden (int): The number of hidden features in the second GATConv layer.
        num_classes (int): The number of output classes.
        heads (int, optional): The number of attention heads in each GATConv layer. Defaults to 6.
    """

    def __init__(self, num_features, num_hidden, num_classes, heads=6):
        super().__init__()
        torch.manual_seed(1234567)
        self.conv1 = GATConv(num_features, 30, heads)
        self.conv2 = GATConv(heads * 30, num_hidden, heads)
        self.linearnet = nn.Linear(num_hidden * heads, num_classes)

    def forward(self, x, edge_index):
        """
        Performs the forward pass of the GAT model with two GATConv layers.

        Args:
            x (torch.Tensor): The input node features.
            edge_index (torch.Tensor): The edge indices representing the graph structure.

        Returns:
            tuple: A tuple containing the output logits (out).
        """

        x = F.dropout(x, p=0.2, training=self.training)
        x = self.conv1(x, edge_index)
        x = F.elu(x)
        x = F.dropout(x, p=0.2, training=self.training)
        h = self.conv2(x, edge_index)
        out = self.linearnet(h)
        return out, h  # Updated return statement to include hidden representation (h)
