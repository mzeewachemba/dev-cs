from sklearn import datasets
import torch
import numpy as np

class MyDataSet(torch.utils.data.Dataset):
    def __init__(self):
        self.all_labels = []
        self.X, self.y = datasets.make_moons(200, noise=0.20)  # entire data

    def __len__(self):
        return len(self.y)

    def __getitem__(self, index):
        # if using cross entropy loss, return following
        # return self.X[index], self.y[index]  # return one pair of data, and its label

        # for MSE loss, return following (there are 2 outputs in the network)
        y2 = np.zeros(2)
        if self.y[index] == 0:
            y2[0] = 0
            y2[1] = 1
        else:
            y2[0] = 1
            y2[1] = 0
        return self.X[index], y2
