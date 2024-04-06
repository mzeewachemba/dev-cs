import sys
#------------------tsne.py----------------
from sklearn.datasets import fetch_openml
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import pandas as pd
import seaborn as sns
import Utils

def main():
    X, y = Utils.read_data()  # cancer data
    
    # randomly select 800 samples from dataset
    np.random.seed(100)
    subsample_idc = np.random.choice(X.shape[0], 800, replace=False) # Generates a random sample of 800 indices from the range of indices of the data
    X = X[subsample_idc, :]
    y = y[subsample_idc]
    y = np.array([int(lbl) for lbl in y])
    
    # applying TSNE
    n_components = 2
    perplexity_list = [10 , 30 , 60 , 80 , 100 , 500 ]
    
    for i in range(len(perplexity_list)):
        perp = perplexity_list[i]
        tsne = TSNE(n_components, perplexity=perp)  
        tsne_result = tsne.fit_transform(X)
    
        print(f'\n Printing tsne_result.shapee \n {tsne_result.shape}')  # 2d for visualization

        plt.title('t-SNE')
        plt.scatter(tsne_result[:, 0], tsne_result[:, 1], s=5, c=y, cmap='Spectral')
        plt.colorbar(boundaries=np.arange(11) - 0.5).set_ticks(np.arange(len(np.unique(y))))
        plt.title(f'TSNE Visualization for TCGA-PANCAN cancer dataset (perplexity used = {perp})')
        plt.show()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
