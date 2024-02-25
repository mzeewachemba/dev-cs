import sys
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import sys
from ucimlrepo import fetch_ucirepo
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import mean_squared_error
from math import sqrt

class KNNClassifier:
    def __init__(self, k=10):
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
        # print(y)
        
        y["Rings"].hist(bins=15)  # plot distribution of rings
        plt.show()
        
        # check for co relation of other features with age
        data = pd.concat([X, y], axis=1)
        # print(data)
        correlation_matrix = data.corr()
        # print(correlation_matrix["Rings"])  # correlation of each column with the rings column

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
            nearest_labels = y_train[nearest_indices]  # Directly index the NumPy array
            majority_class = pd.Series(nearest_labels.flatten()).mode().iloc[0]  # Flatten the array before passing to pd.Series
            y_pred.append(majority_class)
        return np.array(y_pred)



    def evaluate_model(self, y_pred, y_test):
        # print(y_pred)
        # print(y_test)
        # print(np.sum(y_pred == y_test))
        # accuracy = (np.sum(y_pred == y_test) / len(y_test)) * 100
        # print(f"Accuracy: {accuracy:.2f}%")
        count = 0
        for i in range(0,len(y_test)):
            if y_pred[i] == y_test[i]:
                count += 1
        # print(count)
        accuracy = (count) / len(y_test) * 100
        print(f"Accuracy: {accuracy:.2f}%")

    # def evaluate_model(self, y_pred, y_test):
    #     # Print basic information
    #     print(f"Number of test instances: {len(y_test)}")
    #     print(f"Number of correct predictions: {np.sum(y_pred == y_test)}")

    #     # Calculate accuracy
    #     accuracy = accuracy_score(y_test, y_pred)
    #     print(f"Accuracy: {accuracy:.2f}%")

    #     # Print classification report (optional)
    #     print(classification_report(y_test, y_pred))


        
    def visualize_accuracy(self, k_values, accuracies):
        plt.plot(k_values, accuracies, marker='o')
        plt.title('Accuracy vs. Number of Neighbors (k)')
        plt.xlabel('Number of Neighbors (k)')
        plt.ylabel('Accuracy (%)')
        plt.grid(True)
        plt.show()
    
    def plot_predicted_vs_actual(self,ypred, y):
        mean_error = np.sum(np.abs(ypred - y)) / len(y)
        step_size = 20
        a = [ypred[i] for i in range(0, len(ypred)) if i % step_size == 0]
        b = [y[i] for i in range(0, len(ypred)) if i % step_size == 0]
        t = np.linspace(0, len(a), len(a))
        plt.plot(t, a, 'red', linestyle='dashed', label='predicted')
        plt.plot(t, b, 'blue', label='actual')
        plt.scatter(t, a, marker='o', s=10, color="red", label="predicted")
        plt.scatter(t, b, s=10, color="blue", label="actual")
        plt.legend()
        plt.title('mean error =' + str(mean_error))  # title
        plt.show()


    def run(self, dataset_id):
        # Step 1: Load the dataset
        X, y = self.load_dataset(dataset_id)

        # Step 2: Preprocess the data
        X_train, X_test, y_train, y_test = self.preprocess_data(X, y)
        # print(X_test)
        # print(X_test.iloc[0,  :])


        # Step 3: Choose the value of k (number of neighbors)
        # Already set during object initialization

        # Step 4: For each instance in the test set
        distances = self.calculate_distances(X_test.to_numpy(), X_train.to_numpy())
        # distances = np.linalg.norm(X_test.iloc[1, :] - X_train.iloc[1, :])
        # print(distances)
        
        # creating rows and column
        _rows = X_test.index
        _columns = X_train.index
        
        # converting distances into a dataframe
        df_distances = pd.DataFrame(distances, columns=_columns ,index=_rows)
        # print(df_distances)
        
        # classifying
        # Define k value
        k = 50
        
        # Create an empty DataFrame to store results
        predictions_df = pd.DataFrame(columns=["Index", "Mode"])

        # Iterate over each row in distance dataframe
        for index, row in df_distances.iterrows():
            # Extract the least k values from the row
            least_k_values = np.sort(row.values)[:k]
    
            # Find the indices of the k smallest values and sort them
            indices = np.argsort(row.values)[:k]
    
            # Sort the least k values and column names based on the sorted indices
            least_k_values_sorted = least_k_values[np.argsort(indices)]
            kth_column_names_sorted = df_distances.columns[indices][np.argsort(indices)]
    
            # print("Least k values:", least_k_values_sorted)
            # print("Names of columns for least k values:", kth_column_names_sorted)
            
            # DataFrame from least_k_values_sorted and kth_column_names_sorted
            df_least_k_values_sorted = pd.DataFrame(data=least_k_values_sorted, index=kth_column_names_sorted, columns=["Least_k_values_distances"])

            # print(df_least_k_values_sorted)

            # Reset the index of df_least_k_values_sorted to use it as a column for merging
            df_least_k_values_sorted.reset_index(inplace=True)
            
            # Convert y_train to a DataFrame
            df_y_train = pd.DataFrame(y_train, columns=["Rings"])

            # Merge df_least_k_values_sorted with y_test based on their indices
            df_least_k_values_sorted_rings = pd.merge(df_least_k_values_sorted, df_y_train, left_on='index', right_index=True)

            pred_number_of_rings_mode_ = df_least_k_values_sorted_rings['Rings'].mode().values[0]
            # print('mode is:',pred_number_of_rings_mode_)
            # print('index is:',index)
            
            # Store the index and mode in the results DataFrame
            # predictions_df = predictions_df.append({"Index": index, "Mode": pred_number_of_rings_mode_}, ignore_index=True)
            
            new_row = pd.DataFrame({"Index": [index], "Mode": [pred_number_of_rings_mode_]})
            predictions_df = pd.concat([predictions_df, new_row], ignore_index=True)
            
        # Assuming df is your DataFrame
        predictions_df.set_index("Index", inplace=True)
            
        print(predictions_df)
        print(y_test)
        
        
        # y_pred = self.classify_instances(distances, y_train)
        # # print(y_pred)

        # # Step 5: Evaluate the model's performance
        # self.evaluate_model(y_pred, y_test)

        # convert to 1 d
        predictions_df_1d = predictions_df['Mode'].values.flatten()
        # print(predictions_df_1d)

        # # Visualize accuracy for different values of k
        # k_values = [10, 30, 50, 70, 90, 110 , 200 , 300 , 400 , 700 , 1200 ]  # Example values of k
        # accuracies = []
        # for k in k_values:
        #     self.k = k
        #     distances = self.calculate_distances(X_test.to_numpy(), X_train.to_numpy())
        #     y_pred = self.classify_instances(distances, y_train)
        #     # accuracy = np.sum(y_pred == y_test) / len(y_test) * 100
            # count = 0
            # for i in range(0,len(y_test)):
            #     if y_pred[i] == y_test[i]:
            #         count += 1
            # accuracy = (count) / len(y_test) * 100
            # accuracies.append(accuracy)
        # print(accuracies)
        # self.visualize_accuracy(k_values, accuracies)
        
        accuracies = []
        count = 0
        for i in range(0,len(y_test)):
            if predictions_df_1d[i] == y_test[i]:
                count += 1
        accuracy = (count) / len(y_test) * 100
        print('acc is: ', accuracy)

        self.plot_predicted_vs_actual(predictions_df_1d, y_test)


def main():
    knn = KNNClassifier(k=10)  # Initialize KNN classifier with
    knn.run(dataset_id=1)  # Pass the dataset ID to load and run the classifier


if __name__ == "__main__":
    sys.exit(int(main() or 0))

