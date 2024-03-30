import sys
import numpy as np
import matplotlib.pyplot as plt
import umap  # pip install umap-learn
import pandas as pd
import Utils

def main():
    X, y = Utils.read_data()  # cancer data

    # randomly select 800 samples from dataset
    np.random.seed(100)
    subsample_idc = np.random.choice(X.shape[0], 800, replace=False)
    X = X[subsample_idc, :]
    y = y[subsample_idc]
    y = np.array([int(lbl) for lbl in y])

    n_components = 2
    ump = umap.UMAP(
        n_neighbors=30,     # varying min distance
        min_dist=0.1,       # varrying neighbors
        n_components=n_components,
        metric='euclidean'
    )
    umap_result = ump.fit_transform(X)

    print(umap_result.shape)  # 2d for visualization

    plt.title('UMAP')
    plt.scatter(umap_result[:, 0], umap_result[:, 1], s=5, c=y, cmap='Spectral')
    plt.colorbar(boundaries=np.arange(11) - 0.5).set_ticks(np.arange(len(np.unique(y))))
    plt.show()

if __name__ == "__main__":
    sys.exit(int(main() or 0))

