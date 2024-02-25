#-----------Utils.py-------------
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
from numpy import *
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import pandas as pd
 
def load_dataset():
    datafile = "E:/16.Data_for_assignments/CPSC552/TCGA-PANCAN-HiSeq-801x20531/data.csv"
    labels_file = "E:/16.Data_for_assignments/CPSC552/TCGA-PANCAN-HiSeq-801x20531/labels.csv"

    data = np.genfromtxt(
        datafile,
        delimiter=",",
        usecols=range(1, 20532),
        skip_header=1
    )

    true_label_names = np.genfromtxt(
        labels_file,
        delimiter=",",
        usecols=(1,),
        skip_header=1,
        dtype="str"
    )

    print(f'\nshape: \n{data.shape}')
    print(f'\ndata: \n{data}')
    print(f'\ntrue labels: \n{true_label_names[:5]}')
        
    # Encode the true labels into numeric values
    label_encoder = LabelEncoder()
    true_labels_encoded = label_encoder.fit_transform(true_label_names)
    
    # Plot distribution of classes with encoded labels
    plt.figure(figsize=(10, 8))
    plt.hist(true_labels_encoded, bins=range(len(label_encoder.classes_)+1),rwidth=0.8)
    plt.xticks(range(len(label_encoder.classes_)), label_encoder.inverse_transform(range(len(label_encoder.classes_))), rotation='vertical')
    plt.title('Distribution of cancer types')
    plt.ylabel('Frequency')
    plt.xlabel('Cancer Type')
    plt.show()

    X = data
    y = true_labels_encoded
    
    return X, y

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
    
def classify(n_neighbors ,X_train,y_train ,X_test,y_test):
    print(f'\nnumber of neighbors used: {n_neighbors}')
    # Initialize k-NN classifier
    knn_model = KNeighborsRegressor(n_neighbors)

    # Train the classifier
    knn_model.fit(X_train, y_train)
    train_preds = knn_model.predict(X_train)
    mse = mean_squared_error(y_train, train_preds)
    rmse_train = sqrt(mse)
    print('training error = ', rmse_train)

    # Predict the labels for test data
    test_preds = knn_model.predict(X_test)

    # Evaluate accuracy
    accuracy = np.mean(test_preds == y_test) * 100
    print(f"Accuracy: {accuracy:.2f}%")

    mse = mean_squared_error(y_test, test_preds)
    rmse_test = sqrt(mse)
    print('testing error = ', rmse_test)
    
    return accuracy , rmse_train , test_preds, rmse_test

def visualize_accuracy_rmse_vs_neighnors(n_neighbors_array,accuracies ,rmses_train ,rmses_test ):

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7.5, 10))

    # Plot accuracies vs. number of neighbors
    ax1.plot(n_neighbors_array, accuracies, marker='o', linestyle='dashed', color='red', label='Accuracy')
    ax1.plot(n_neighbors_array, rmses_train, marker='o', linestyle='dotted', color='blue', label='Train RMSE')
    ax1.set_title('Accuracy , train RMSE vs. Number of Neighbors (k)')
    ax1.set_xlabel('Number of Neighbors (k)')
    ax1.set_ylabel('Accuracy (%) , , train RMSE ')
    ax1.legend()
    ax1.grid(True)

    # Plot RMSE for training set vs. number of neighbors
    ax2.plot(n_neighbors_array, accuracies, marker='o', linestyle='dashed', color='red', label='Accuracy')
    ax2.plot(n_neighbors_array, rmses_test, marker='o', linestyle='solid', color='green', label='Test RMSE')
    ax2.set_title('Accuracy , test RMSE vs. Number of Neighbors (k)')
    ax2.set_xlabel('Number of Neighbors (k)')
    ax2.set_ylabel('Accuracy (%) , , test RMSE ')
    ax2.legend()
    ax2.grid(True)

    # Adjust layout
    plt.tight_layout()

    # Show the plots
    plt.show()
    
