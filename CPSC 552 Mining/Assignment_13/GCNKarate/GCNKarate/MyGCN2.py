from torch_geometric.nn import GCNConv
from torch import nn


class MyGCN2(nn.Module):  # 2 layer GCN
    """
    A custom GCN (Graph Convolutional Network) model with two GCN layers.

    This class defines a GCN model with two GCN layers followed by a linear layer for classification.

    Args:
        num_features (int): The number of input features per node.
        num_hidden (int): The number of hidden features in the first GCN layer.
        num_classes (int): The number of output classes.
    """

    def __init__(self, num_features, num_hidden, num_classes):
        super().__init__()
        self.gcn1 = GCNConv(num_features, num_hidden)
        self.gcn2 = GCNConv(num_hidden, num_classes)
        self.linearnet = nn.Linear(num_classes, num_classes)  # Updated output dimension

    def forward(self, x, edge_index):
        """
        Performs the forward pass of the GCN model with two GCN layers.

        Args:
            x (torch.Tensor): The input node features.
            edge_index (torch.Tensor): The edge indices representing the graph structure.

        Returns:
            tuple: A tuple containing the hidden representation (h2) and the output logits.
        """

        h1 = self.gcn1(x, edge_index).relu()
        h2 = self.gcn2(h1, edge_index).relu()
        out = self.linearnet(h2)
        return h2, out
