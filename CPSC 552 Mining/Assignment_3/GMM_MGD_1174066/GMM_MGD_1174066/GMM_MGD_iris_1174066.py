import numpy as np
import pandas as pd
import sys
from scipy.stats import mode
import matplotlib.pyplot as plt


def calculate_gaussian_probability(data, mu, covariance, num_of_features):
    variance_xmu = np.matrix(data - mu)
    exponent = np.exp(-0.5 * variance_xmu @ np.linalg.inv(covariance) @ variance_xmu.T)
    denom = 1 / np.sqrt(((2*np.pi)**num_of_features) * np.linalg.det(covariance))
    gmm_normal_distribution = denom * exponent
    return gmm_normal_distribution


def expectation_step(data, mu, covariance, num_of_features, num_clusters, phi, gamma, n):
    for i in range(0, n):
        denom = 0
        for j in range(0, num_clusters):
            denom += phi[j] * calculate_gaussian_probability(data[i, :], mu[j], covariance[j], num_of_features)
        for k in range(0, num_clusters):
            gamma[i, k] = (phi[k] * calculate_gaussian_probability(data[i, :], mu[k], covariance[k],num_of_features)[0, 0]) / denom


def maximization_step(data, mu, covariance, num_of_features, num_clusters, phi, gamma, n):
    new_phi = np.mean(gamma, axis=0)
    sumgk = np.sum(gamma, axis=0)
    new_mu = np.zeros((num_clusters, num_of_features))
    new_covariance = np.zeros((num_clusters, num_of_features, num_of_features))
    
    for k in range(num_clusters):
        for i in range(n):
            new_mu[k] += (data[i, :] * gamma[i, k])
        new_mu[k] /= sumgk[k]
        for i in range(n):
            variance = np.matrix(data[i, :] - new_mu[k])
            new_covariance[k] += (variance.T @ variance) * gamma[i, k]
        new_covariance[k] /= sumgk[k]
    
    return new_phi, new_mu, new_covariance


def plot_iris(data, num_clusters):
    plt.figure(figsize=(10, 6))
    plt.title('Gaussian Multi Model Clusters')
    plt.scatter(
        data[:,0],
        data[:,2],
        c=num_clusters,
        cmap = plt.colormaps.get_cmap('brg'),
        marker='.')
    plt.tight_layout()
    plt.show()
    # print('data 0 is:++++++++',data[:,0])
    # print('data 2 is:++++++++',data[:,2])

    
def main():
    # INITIALIZE DATA
    df = pd.read_csv("E:/16.Data_for_assignments/CPSC552/iris.csv")
    # print(df.head(10))
    dfrandom = df
    
    # Extract features and training data
    df1_random = dfrandom.iloc[:, 0:4].astype(float)
    dftrain = df1_random.values
    dftrain = dftrain[:, 0:4]
    # print(dftrain)

    # GMM PARAMETERS
    num_clusters = 3
    num_of_features = 4
    n = dftrain.shape[0]
    np.random.seed(42)
    mu = np.zeros((num_clusters, num_of_features))
    covariance = np.zeros((num_clusters, num_of_features, num_of_features))

    random_row = np.random.randint(low=0, high=150, size=num_clusters)
    mu = np.array([dftrain[row, :] for row in random_row])
    mean_from_data = np.mean(dftrain, axis=0)
    variance_xmean = np.matrix(dftrain - mean_from_data)
    covariance = np.array([variance_xmean.T @ variance_xmean / n for c in range(num_clusters)])

    phi = np.ones((num_clusters)) / num_clusters
    gamma = np.zeros((n, num_clusters))
    
    # printing initial parameters
    print(phi)
    print(mu)
    print(covariance)
  
    # TRAINING
    num_iterations = 20

    for iter_num in range(num_iterations):
        expectation_step(dftrain, mu, covariance, num_of_features, num_clusters, phi, gamma, n)
        phi, mu, covariance = maximization_step(dftrain, mu, covariance, num_of_features, num_clusters, phi, gamma, n)
        print('----------------iteration =', iter_num)

    #FINAL PARAMETERS CHECKING
    print(mu)
    print(gamma)
    print(phi)
    
    # CALCULATING PREDICTIONS
    preds = []
    for i in range(n):
        pred = np.argmax(np.multiply(gamma[i, :], phi))
        preds.append(pred)
    print(preds)
    
    #plotting the data
    plot_iris(dftrain, preds)

    # checking if our predictions are present in the clusters
    cluster_assigned = [mode(preds[0:50])[0], mode(preds[50:100])[0], mode(preds[100:150])[0]]
    acc = 0
    for i in range(n):
        if preds[i] == cluster_assigned[0] and i < 50:
            acc += 1
        if preds[i] == cluster_assigned[1] and 50 <= i < 100:
            acc += 1
        if preds[i] == cluster_assigned[2] and 100 <= i < 150:
            acc += 1

    print('accuracy =', acc / n * 100)


if __name__ == "__main__":
    sys.exit(int(main() or 0))
