import sys
import Utils

def main():
    # Load the data
    X , y =  Utils.load_dataset()


    # Split the data into train and test sets
    X_train, X_test, y_train, y_test = Utils.get_train_test_data(X, y)

    # --------------using knn in sklearn-------
    #initializing neighbors - test for 5 neighbors
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


