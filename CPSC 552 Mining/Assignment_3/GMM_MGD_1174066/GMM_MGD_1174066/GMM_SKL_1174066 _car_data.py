      #------------------GMM_SKL.py-----------------------
import sklearn 
from sklearn.mixture import GaussianMixture
import numpy as np
from scipy import stats
import sys
import pandas as pd
from scipy.stats import mode
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt



def main():
    # ---------------Car evaluation Dataset-------------
    df = pd.read_csv("E:/16.Data_for_assignments/CPSC552/car.data")
    
    #assigning column names to the data
    df.columns = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety','class']

    # Preprocess convert categorical variables to numerical using Label Encoding
    label_encoder = LabelEncoder()
    df['buying'] = label_encoder.fit_transform(df['buying'])
    df['maint'] = label_encoder.fit_transform(df['maint'])
    df['doors'] = label_encoder.fit_transform(df['doors'])
    df['persons'] = label_encoder.fit_transform(df['persons'])
    df['lug_boot'] = label_encoder.fit_transform(df['lug_boot'])
    df['safety'] = label_encoder.fit_transform(df['safety'])
    df['class'] = label_encoder.fit_transform(df['class'])
    
    # ---randomize data
    dfrandom = df  # df.sample(frac=1, random_state=1119).reset_index(drop=True)
    # data read from a file is read as a string, so convert the first 4 cols to float
    df1 = dfrandom.iloc[:, 0:6].astype(float)
    # ---separate out the last column
    df2 = dfrandom.iloc[:, 6]
    # ---combine the 4 numerical columns and the last column that has the flower category
    dfrandom = pd.concat([df1, df2], axis=1)
    print(dfrandom)
    
    # --------------GMM-----------------
    xdata = df1.values[:, 0:6]
    print(xdata.shape)
    N = xdata.shape[0]
    
    gm = GaussianMixture(n_components=3, max_iter=20)
    gm.fit(xdata)                                                                             
    print(gm.means_)
    print(gm.weights_)
    print(gm.covariances_)
    z = gm.score(xdata)
    print(z)

    # -----compute accuracy--------
    preds = gm.predict(xdata)
    print(preds)
    cluster_assigned = []
    
    # since GMM is unsupervised, class assignments to clusters may vary on each run
    cluster_assigned = [mode(preds[0:300])[0], mode(preds[300:600])[0], mode(preds[600:900])[0] ,mode(preds[900:1200])[0] ,mode(preds[1200:1500])[0] ,mode(preds[1500:1727])[0]]
    acc = 0
    #checking if our predictions are present in the clusters
    for i in range(N):
        if preds[i] == cluster_assigned[0] and i < 300:
            acc += 1
        if preds[i] == cluster_assigned[1] and 300 <= i < 600:
            acc += 1
        if preds[i] == cluster_assigned[2] and 600 <= i < 900:
            acc += 1
        if preds[i] == cluster_assigned[3] and 900 <= i < 1200:
            acc += 1
        if preds[i] == cluster_assigned[4] and 1200 <= i < 1500:
            acc += 1
        if preds[i] == cluster_assigned[5] and 1500 <= i < 1727:
            acc += 1

    print('accuracy =', acc / N * 100)
    
    # -------------- Scatter Plot --------------
    plt.figure(figsize=(10, 6))
    plt.title('Scatter Plot of GMM Clusters')
    plt.scatter(xdata[:, 0], xdata[:, 1], c=preds, cmap='viridis')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.colorbar(label='Cluster')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    sys.exit(int(main() or 0))


