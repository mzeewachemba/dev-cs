import Utils
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import sys

def main():
    # loading data
    dataset_id = 1
    X , y = Utils.load_dataset(dataset_id)
    print('\n',X.head(6))
    print('\n',y.head(6))
    
    # pre process data
    X , y = Utils.preprocess_data( X, y)
    # print(X.head(6))
    # print(y.head(6))

    #convert X and y to numpy
    X = X.values 
    y = y.values


    # ------test KNN on an unknown data point----------

    new_data_point = np.array([
        0.417,  # length
        0.396,  # diameter
        0.134,  # height
        0.816,  # whole weight
        0.383,  # shucked weight
        0.172,  # viscera weight
        0.221,  # shell weight
    ])

    Utils.knn_predict_single_data_point(X, y, new_data_point, 3)  #test for k = 3  for sample point
    Utils.knn_predict_single_data_point(X, y, new_data_point, 7)  #test for k = 7  for sample point

    # get train, test data using scikit's train_test_split
    X_train, X_test, y_train, y_test = Utils.get_train_test_data(X, y)
    
    # --------------using knn in sklearn-------
    #initializing neighbors - test for one neignbor
    n_neighbors = 5

    accuracy , rmse_train , test_preds, rmse_test = Utils.classify(n_neighbors ,X_train,y_train ,X_test,y_test)

    Utils.plot_predicted_vs_actual(test_preds, y_test)

    # try different values of n_neighbors to see if error drops
    n_neighbors_array = [1 ,  3  , 5 , 10 ,15 , 20 , 25 , 50 , 100 , 150 , 200 , 250]  # Example values of k
    accuracies = []
    rmses_train = []
    rmses_test = []

    for k in n_neighbors_array:
        accuracy , rmse_train , test_preds, rmse_test = Utils.classify(k ,X_train,y_train ,X_test,y_test)
        accuracies.append(accuracy)
        rmses_train.append(rmse_train)
        rmses_test.append(rmse_test)

    # Visualize accuracy and errors for different values of k
    Utils.visualize_accuracy_rmse_vs_neighnors(n_neighbors_array,accuracies ,rmses_train ,rmses_test )


if __name__ == "__main__":
    sys.exit(int(main() or 0))
