import numpy as np
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt
from MyDataSet import MyDataSet
import torch

def visualize_data(self, X, y):
    plt.scatter(X[:,0], X[:,1], s=40, c=y, cmap=plt.cm.Spectral)
    plt.show()
    return X, y

def get_data_loader(batch_size=4):
    dataset = MyDataSet()
    data_loader = torch.utils.data.DataLoader(
        dataset, batch_size=batch_size, shuffle=True)
    return data_loader

def plot_decision_boundary(net, X, y , no_layers):
    # set min and max values
    x_min, x_max = -2.5, 2.5
    y_min, y_max = -2.5, 2.5
    h = 0.02
    # Generate a grid of points with distance h between them
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    # Predict the predicted value for the whole grid
    xdata = np.c_[xx.ravel(), yy.ravel()]
    Z = net(torch.tensor(xdata).type(torch.float32).cuda())  # outputs for mesh data
    Z = np.array(Z.cpu().detach())
    Z = np.argmax(Z, axis=1)
    Z = Z.reshape(xx.shape)
    # Plot the contour and training data points
    plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Spectral)
    plt.title(f"Number of layers used {no_layers}")
    plt.show()
