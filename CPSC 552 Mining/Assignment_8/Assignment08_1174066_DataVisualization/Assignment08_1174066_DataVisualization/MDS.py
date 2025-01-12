import sys
from sklearn.datasets import load_digits
from sklearn.manifold import MDS
import Utils
import numpy as np
import matplotlib.pyplot as plt

def main():
    X, y = Utils.read_data()  # cancer data
    
    # randomly select 800 samples from dataset
    np.random.seed(100)
    subsample_idc = np.random.choice(X.shape[0], 800, replace=False)  #  Generates a random sample of 800 indices from the range of indices of the data 
    X = X[subsample_idc, :]
    y = y[subsample_idc]
    y = np.array([int(lbl) for lbl in y])
    
    num_components = 2
    mds = MDS(n_components=num_components, normalized_stress='auto') # applying mds algorithms to reduce number of components
    X_reduced = mds.fit_transform(X)
    
    print(f'\n Printing X_reduced.shape \n {X_reduced.shape}')
    
    plt.scatter(X_reduced[:, 0], X_reduced[:, 1], s=5, c=y, cmap='Spectral')
    plt.colorbar(boundaries=np.arange(11) - 0.5).set_ticks(np.arange(len(np.unique(y))))
    plt.title('MDS Visualization for TCGA-PANCAN cancer dataset')
    plt.show()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
