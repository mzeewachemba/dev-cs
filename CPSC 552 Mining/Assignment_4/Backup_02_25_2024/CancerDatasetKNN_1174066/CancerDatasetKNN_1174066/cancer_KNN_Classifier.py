import Utils
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from math import sqrt
import sys

def main():
    # loading data
    X, y = Utils.load_dataset()

    
    # # pre process data
    # X , y = Utils.preprocess_data( X, y)
    # # print(X.head(6))
    # # print(y.head(6))

    # #convert X and y to numpy
    # X = X.values 
    # y = y.values


    # # ------test KNN on an unknown data point----------

    # new_data_point = np.array([
    #     0.417,  # length
    #     0.396,  # diameter
    #     0.134,  # height
    #     0.816,  # whole weight
    #     0.383,  # shucked weight
    #     0.172,  # viscera weight
    #     0.221,  # shell weight
    # ])

    # Utils.knn_predict_single_data_point(X, y, new_data_point, 3)  #test for k = 3
    # Utils.knn_predict_single_data_point(X, y, new_data_point, 7)  #test for k = 7

    # --------------using knn in sklearn-------
    # get train, test data using scikit's train_test_split
    X_train, X_test, y_train, y_test = Utils.get_train_test_data(X, y)
    knn_model = KNeighborsRegressor(n_neighbors=5)
    knn_model.fit(X_train, y_train)
    train_preds = knn_model.predict(X_train)
    mse = mean_squared_error(y_train, train_preds)
    rmse = sqrt(mse)
    print('\ntraining error = ', rmse)
    test_preds = knn_model.predict(X_test)
    mse = mean_squared_error(y_test, test_preds)
    rmse = sqrt(mse)
    print('\ntesting error = ', rmse)
    Utils.plot_predicted_vs_actual(test_preds, y_test)
    # try different values of n_neighbors to see if error drops


if __name__ == "__main__":
    sys.exit(int(main() or 0))
