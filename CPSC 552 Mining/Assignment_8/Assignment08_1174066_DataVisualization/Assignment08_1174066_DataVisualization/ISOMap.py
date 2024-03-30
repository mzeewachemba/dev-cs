import sys
from sklearn.datasets import load_digits
from sklearn.manifold import Isomap
import Utils
import numpy as np
import matplotlib.pyplot as plt

def main():
    X, y = Utils.read_data()  # cancer data
    
    # randomly select 800 samples from dataset
    np.random.seed(100)
    subsample_idc = np.random.choice(X.shape[0], 800, replace=False)
    X = X[subsample_idc, :]
    y = y[subsample_idc]
    y = np.array([int(lbl) for lbl in y])
    
    num_components = 2
    isomap = Isomap(n_components=num_components)
    X_reduced = isomap.fit_transform(X)
    
    print(X_reduced.shape)
    
    plt.title('ISOMAP')
    plt.scatter(X_reduced[:, 0], X_reduced[:, 1], s=5, c=y, cmap='Spectral')
    plt.colorbar(boundaries=np.arange(11) - 0.5).set_ticks(np.arange(len(np.unique(y))))
    plt.show()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
