from torch_geometric.nn import GCNConv
from torch import nn


class MyGCN(nn.Module):
    """
    A custom GCN (Graph Convolutional Network) model.

    This class defines a GCN model with one GCN layer followed by a linear layer for classification.

    Args:
        num_features (int): The number of input features per node.
        num_hidden (int): The number of hidden features in the GCN layer.
        num_classes (int): The number of output classes.
    """

    def __init__(self, num_features, num_hidden, num_classes):
        super().__init__()
        self.gcn = GCNConv(num_features, num_hidden)
        self.linearnet = nn.Linear(num_hidden, num_classes)

    def forward(self, x, edge_index):
        """
        Performs the forward pass of the GCN model.

        Args:
            x (torch.Tensor): The input node features.
            edge_index (torch.Tensor): The edge indices representing the graph structure.

        Returns:
            tuple: A tuple containing the hidden representation (h) and the output logits.
        """

        h = self.gcn(x, edge_index).relu()
        out = self.linearnet(h)
        return h, out
