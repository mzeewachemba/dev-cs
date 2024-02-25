import sys
from ucimlrepo import fetch_ucirepo
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import numpy as np


def main():
    # LOADING DATASET
    # fetch dataset
    abalone = fetch_ucirepo(id=1)

    # data (as pandas dataframes)
    X = abalone.data.features
    label_encoder = LabelEncoder()
    X.loc[:, 'Sex'] = label_encoder.fit_transform(X['Sex']).astype(float)
    y = abalone.data.targets

    # PROCESSING DATASET
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, train_size=0.8, shuffle=False)
    X_train['Sex'] = label_encoder.fit_transform(X_train['Sex'])  # convert categorical variables to numerical using Label Encoding

    # Convert DataFrame to NumPy array
    X_train_array = X_train.to_numpy()
    X_test_array = X_test.to_numpy()

    # SETTING number of neighbors
    k = 50

    # Convert all elements to numeric data type
    X_train_array = X_train_array.astype(float)
    X_test_array = X_test_array.astype(float)

    # calculating distance for each test instance and all training instances
    distances = np.linalg.norm(X_test_array[:, np.newaxis, :] - X_train_array[np.newaxis, :, :], axis=2)

    # Classify test instances based on majority vote of nearest neighbors
    y_pred = []

    for i in range(X_test_array.shape[0]):
        # Get indices of k nearest neighbors for the current test instance
        nearest_indices = np.argsort(distances[i])[:k]

        # Get corresponding labels of the k nearest neighbors
        nearest_labels = y_train[nearest_indices]

        # Determine the majority class among the k nearest neighbors
        majority_class = np.bincount(nearest_labels).argmax()

        # Assign the test instance to the majority class
        y_pred.append(majority_class)

    y_pred = np.array(y_pred)

    # Calculate accuracy
    accuracy = np.sum(y_pred == y_test) / len(y_test) * 100
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    sys.exit(int(main() or 0))
