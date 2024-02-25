import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from ucimlrepo import fetch_ucirepo


class KNNClassifier:
    def __init__(self, k=5):
        self.k = k

    def load_dataset(self, dataset_id):
        abalone = fetch_ucirepo(id=dataset_id)
        X = abalone.data.features
        y = abalone.data.targets
        return X, y

    def preprocess_data(self, X, y):
        # Handle missing values if any
        X = X.ffill()

        X = X.drop("Sex", axis=1)  # this column may not contribute to age prediction

        y["Rings"].hist(bins=15)  # plot distribution of rings
        plt.show()

        # Split the dataset into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, train_size=0.8, shuffle=False)

        # Convert y_train and y_test to NumPy arrays
        y_train = y_train.to_numpy()
        y_test = y_test.to_numpy()

        return X_train, X_test, y_train, y_test

    def calculate_distances(self, X_test, X_train):
        return np.linalg.norm(X_test[:, np.newaxis, :] - X_train[np.newaxis, :, :], axis=2)

    def classify_instances(self, distances, y_train):
        y_pred = []
        for i in range(distances.shape[0]):
            nearest_indices = np.argsort(distances[i])[:self.k]
            nearest_labels = y_train[nearest_indices]
            majority_class = pd.Series(nearest_labels.flatten()).mode().iloc[0]
            y_pred.append(majority_class)
        return np.array(y_pred)

    def evaluate_model(self, y_pred, y_test):
        count = 0
        for i in range(0, len(y_test)):
            if y_pred[i] == y_test[i]:
                count += 1
        accuracy = (count) / len(y_test) * 100
        print(f"Accuracy: {accuracy:.2f}%")

    def plot_predicted_vs_actual(self, y_pred, y):
        mean_error = np.sum(np.abs(y_pred - y)) / len(y)
        step_size = 20
        t = np.linspace(0, len(y_pred), len(y_pred))
        plt.plot(t[::step_size], y_pred[::step_size], 'red', linestyle='dashed', label='predicted')
        plt.plot(t[::step_size], y[::step_size], 'blue', label='actual')
        plt.scatter(t[::step_size], y_pred[::step_size], marker='o', s=10, color="red", label="predicted")
        plt.scatter(t[::step_size], y[::step_size], s=10, color="blue", label="actual")
        plt.legend()
        plt.title('Mean Error =' + str(mean_error))
        plt.show()

    def run(self, dataset_id):
        X, y = self.load_dataset(dataset_id)
        X_train, X_test, y_train, y_test = self.preprocess_data(X, y)
        distances = self.calculate_distances(X_test.to_numpy(), X_train.to_numpy())

        y_pred = self.classify_instances(distances, y_train)
        self.evaluate_model(y_pred, y_test)

        self.plot_predicted_vs_actual(y_pred, y_test)


def main():
    knn = KNNClassifier(k=3)  # Initialize KNN classifier with k=3
    knn.run(dataset_id=1)  # Pass the dataset ID to load and run the classifier


if __name__ == "__main__":
    main()
