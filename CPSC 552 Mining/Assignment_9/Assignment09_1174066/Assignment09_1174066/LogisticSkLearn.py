import sys
from Utils import Utils
import numpy as np
from sklearn.linear_model import LogisticRegression

def main():
    utils = Utils()
    data = utils.readDataRandom()  # load data
    X = data[:, 0:2]  # use only two features, for visualization purposes
    Y = data[:, -1]  # expected output, -1 means last column
    model = LogisticRegression(solver='lbfgs')
    model.fit(X, Y)
    preds = model.predict(X)  # predictions by the trained model
    accuracy = (preds == Y).mean()
    print("Number of correct predictions = ", str(np.sum(Y == preds.reshape(Y.shape[0])) / len(X) * 100) + '%')
    print("Accuracy SKL= " + str(accuracy))
    print(model.intercept_, model.coef_)

if __name__ == "__main__":
    sys.exit(int(main() or 0))

