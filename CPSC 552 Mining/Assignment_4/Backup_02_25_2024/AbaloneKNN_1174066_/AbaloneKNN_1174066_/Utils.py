#-----------Utils.py-------------
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
from numpy import *
from ucimlrepo import fetch_ucirepo
import scipy.stats
 
def load_dataset(dataset_id):
    abalone = fetch_ucirepo(id=dataset_id)
    X = abalone.data.features
    y = abalone.data.targets
    return X, y

def preprocess_data( X, y):
    # Handle missing values if any
    X = X.ffill()

    X = X.drop("Sex", axis=1)  # this column may not contribute to age prediction

    y["Rings"].hist(bins=15)  # plot distribution of rings
    plt.show()
    
    # see if the different features are correlated to age positive or negative correlation between the features
    # and the target helps in better prediction
    data = pd.concat([X, y], axis=1)
    # print(data)
    correlation_matrix = data.corr()
    print(correlation_matrix["Rings"])  # correlation of each column with the rings column

    return X, y

def knn_predict_single_data_point(X, y, new_data_point, k):
    # Calculate distances between new data point and all data points in X
    distances = np.linalg.norm(X - new_data_point, axis=1)
    # Find the indices of the k nearest neighbors
    nearest_neighbor_ids = distances.argsort()[:k]
    print(nearest_neighbor_ids)
    # Extract the target values of the k nearest neighbors
    nearest_neighbor_rings = y[nearest_neighbor_ids]
    print(nearest_neighbor_rings)
    # Calculate the mean of the target values as the prediction
    prediction = nearest_neighbor_rings.mean()
    print(f'predicted number of rings k={k}, prediction={prediction}\n')
    mode = scipy.stats.mode(nearest_neighbor_rings)
    print(f'Predicted rings, using mode with k = {k}, # rings={mode[0]}\n')

def get_train_test_data(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=12345)
    return X_train, X_test, y_train, y_test


def plot_predicted_vs_actual(ypred, y):
    mean_error = sum(abs(ypred - y)) / len(y)
    step_size = 20
    a = [ypred[i] for i in range(0, len(ypred)) if i % step_size == 0]
    b = [y[i] for i in range(0, len(ypred)) if i % step_size == 0]
    t = linspace(0, len(a), len(a))
    plt.plot(t, a, 'red', linestyle='dashed', label='predicted')
    plt.plot(t, b, 'blue', label='actual')
    plt.scatter(t, a, marker='o', s=10, color="red", label="predicted")
    plt.scatter(t, b, s=10, color="blue", label="actual")
    plt.legend()
    plt.title('mean error =' + str(mean_error))  # title
    plt.show()
