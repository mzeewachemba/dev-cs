import numpy as np
import Utils
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.neighbors import KNeighborsRegressor



# Load the data
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

# Encode the true labels into numeric values
label_encoder = LabelEncoder()
true_labels_encoded = label_encoder.fit_transform(true_label_names)

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(data, true_labels_encoded, test_size=0.2, random_state=12345)

# Initialize k-NN classifier
knn_model = KNeighborsRegressor(n_neighbors=5)

# Train the classifier
knn_model.fit(X_train, y_train)
train_preds = knn_model.predict(X_train)
mse = mean_squared_error(y_train, train_preds)
rmse = sqrt(mse)
print('\ntraining error = ', rmse)

# Predict the labels for test data
test_preds = knn_model.predict(X_test)

# Evaluate accuracy
accuracy = np.mean(test_preds == y_test) * 100
print(f"Accuracy: {accuracy:.2f}%")

mse = mean_squared_error(y_test, test_preds)
rmse = sqrt(mse)
print('\ntesting error = ', rmse)
Utils.plot_predicted_vs_actual(test_preds, y_test)
# try different values of n_neighbors to see if error drops

