import sys
from torch_geometric.datasets import Planetoid  # Cora Planetoid dataset
from torch_geometric.transforms import NormalizeFeatures
from MyGCN import MyGCN
from MyGATCN import MyGATCN
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import umap
import torch
from matplotlib.colors import ListedColormap


def visualize_TSNE_nodes(h, color):
    """
    Visualizes node embeddings using t-SNE dimensionality reduction.

    Args:
        h (torch.Tensor): The node embeddings.
        color (list): The node colors used for visualization.
    """

    z = TSNE(n_components=2).fit_transform(h.detach().cpu().numpy())
    plt.figure(figsize=(10, 10))
    plt.title('Visualization of Node Embedding - TSNE')
    plt.xticks([])
    plt.yticks([])
    plt.scatter(z[:, 0], z[:, 1], s=10, c=color, cmap="Set2")
    plt.show()


def visualize_UMAP_nodes(h, color):
    """
    Visualizes node embeddings using UMAP dimensionality reduction.

    Args:
        h (torch.Tensor): The node embeddings.
        color (list): The node colors used for visualization.
    """

    z = umap.UMAP(n_neighbors=5, n_components=2,
                   min_dist=0.3,
                   metric='correlation').fit_transform(h.detach().cpu().numpy())
    plt.figure(figsize=(10, 10))
    plt.title('Visualization of Node Embedding - UMAP')
    plt.xticks([])
    plt.yticks([])
    plt.scatter(z[:, 0], z[:, 1], s=10, c=color, cmap="Set2")
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


def plot_embeddings(data, embeddings):
    """
    Visualizes node embeddings in 3D space.

    Args:
        data (torch_geometric.data.Data): The graph data object.
        embeddings (np.ndarray): The node embeddings.
    """

    custom_colors = ['blue', 'yellow', 'green', 'black',
                      'red', 'purple', 'orange']
    custom_cmap = ListedColormap(custom_colors)
    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(projection='3d')
    ax.patch.set_alpha(0)
    plt.tick_params(left=False,
                    bottom=False,
                    labelleft=False,
                    labelbottom=False)
    ax.scatter(embeddings[:, 0], embeddings[:, 1], embeddings[:, 2],
               s=5, c=data.y, cmap=custom_cmap, vmin=-2, vmax=3)
    plt.show()
def main():
    """
    Main function for training and evaluating a GCN model on the Cora dataset.

    This function loads the Cora dataset, defines a GCN model, trains the model,
    evaluates its performance, and visualizes the learned node embeddings.
    """

    dataset = Planetoid(root='data/Planetoid',
                         name='Cora',
                         transform=NormalizeFeatures())
    # 2708 nodes with 1433 features in each node
    # 1 if the word is included in the paper else 0.
    # 7 classes
    # 0: "Theory",
    # 1: "Reinforcement_Learning",
    # 2: "Genetic_Algorithms",
    # 3: "Neural_Networks",
    # 4: "Probabilistic_Methods",
    # 5: "Case_Based",
    # 6: "Rule_Learning"

    print(f'Number of features: {dataset.num_features}')
    print(f'Number of classes: {dataset.num_classes}')

    data = dataset[0]  # First graph object.
    print(data)

    # model = MyGCN(num_features=data.num_features, num_hidden=16, num_classes=7)
    # Uncomment the following line to use MyGATCN instead of MyGCN
    model = MyGATCN(num_features=data.num_features, num_hidden=16, num_classes=7)

    print(model)

    model.eval()
    out, _ = model(data.x, data.edge_index)

    # Uncomment these lines to visualize embeddings using UMAP or t-SNE
    # visualize_TSNE_nodes(out, color=data.y)
    # visualize_UMAP_nodes(out, color=data.y)

    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.02)
    num_epochs = 200

    # Train GCN
    model.train()
    for epoch in range(num_epochs):
        optimizer.zero_grad()
        out, h = model(data.x, data.edge_index)  # h is learnt embedding
        # print(h.shape)  # Commented out to avoid unnecessary print
        loss = criterion(out, data.y)
        acc = compute_accuracy(out.argmax(dim=1), data.y)
        loss.backward()
        optimizer.step()
        if epoch % 10 == 0:
            print(f'Epoch {epoch:>3} | Loss: {loss:.2f} | Acc: {acc*100:.2f}%')

    # Plot final learnt embedding for each train node
    plot_embeddings(data, h.detach().cpu().numpy())

    # Visualize embeddings using UMAP and t-SNE (uncomment desired lines)
    visualize_UMAP_nodes(out, color=data.y)
    visualize_TSNE_nodes(out, color=data.y)


if __name__ == "__main__":
    sys.exit(int(main() or 0))

