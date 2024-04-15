import numpy as np
import sys

# pip install networkx
# pip install torch-geometric
from torch_geometric.datasets import KarateClub
import matplotlib.pyplot as plt
import networkx as nx
from torch_geometric.utils import to_networkx
from MyGCN import MyGCN
from MyGCN2 import MyGCN2 # 2 layer GCN
import torch
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"


def plot_graph(data):
    """
    Plots the graph data using NetworkX.

    Args:
        data (torch_geometric.data.Data): The graph data object.
    """

    G = to_networkx(data, to_undirected=True)
    plt.figure(figsize=(12, 12))
    plt.axis('off')
    nx.draw_networkx(G,
                     pos=nx.spring_layout(G, seed=0),
                     with_labels=True,
                     node_size=800,
                     node_color=data.y,
                     cmap="hsv",
                     vmin=-2,
                     vmax=3,
                     width=0.8,
                     edge_color="grey",
                     font_size=14
                     )
    plt.show()


def plot_embeddings(data, embeddings):
    """
    Plots the node embeddings in 3D space.

    Args:
        data (torch_geometric.data.Data): The graph data object.
        embeddings (np.ndarray): The node embeddings.
    """

    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(projection='3d')
    ax.patch.set_alpha(0)
    plt.tick_params(left=False,
                    bottom=False,
                    labelleft=False,
                    labelbottom=False)
    ax.scatter(embeddings[:, 0], embeddings[:, 1], embeddings[:, 2],
               s=200, c=data.y, cmap="hsv", vmin=-2, vmax=3)
    plt.show()


def compute_accuracy(actual_y, expected_y):
    """
    Computes the accuracy between predicted and actual labels.

    Args:
        actual_y (torch.Tensor): The actual labels.
        expected_y (torch.Tensor): The predicted labels.

    Returns:
        float: The accuracy (percentage of correctly classified nodes).
    """

    return (expected_y == actual_y).sum() / len(actual_y)


def main():
    """
    The main function to train and evaluate the GCN model on the Karate Club dataset.
    """

    dataset = KarateClub()

    # Print information
    print(dataset)
    print('------------')
    print(f'Number of graphs: {len(dataset)}')
    print(f'Number of features: {dataset.num_features}')
    print(f'Number of classes: {dataset.num_classes}')
    print(f'Graph: {dataset[0]}')
    # 34 nodes with each node having 34 features, 78 edges

    data = dataset[0]
    print(data.x)  # identity matrix, the node itself does not
    # contain any info in this example, but can contain features
    # such as age, weight, height
    print(data.edge_index)  # 2x78 = 156 edges
    # we will use edge info to classify a node
    # edge indicates which node is connected to which node
    # e.g., 0 -> 1,2,3,4,5,6,7,8,10

    print(data.y)  # 34 values
    print(data.train_mask)  # true to use for training, false for testing

    plot_graph(data)

    # model = MyGCN(num_features=34, num_hidden=3, num_classes=4)
    model = MyGCN2(num_features=34,num_hidden=3,num_classes=4)
    print(model)

    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.02)
    num_epochs = 100

    # Train GCN
    for epoch in range(num_epochs):
        optimizer.zero_grad()
        h, out = model(data.x, data.edge_index)  # h is learnt embedding
        # print(h.shape)
        loss = criterion(out, data.y)
        acc = compute_accuracy(out.argmax(dim=1), data.y)
        loss.backward()
        optimizer.step()
        if epoch % 10 == 0:
            print(f'Epoch {epoch:>3} | Loss: {loss:.2f} | Acc: {acc*100:.2f}%')

    # plot final learnt embedding for each train node
    plot_embeddings(data, h.detach().cpu().numpy())

if __name__ == "__main__":
    sys.exit(int(main() or 0))

