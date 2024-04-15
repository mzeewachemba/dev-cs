import torch
from torch.utils.data import Dataset
import pandas as pd
import numpy as np


class TestDataset(Dataset):
    def __init__(self, test_file, transform=None):
        """
        Initializes a TestDataset object.

        Args:
            test_file (str): Path to the CSV file containing test data.
            transform (callable, optional): A function to be applied to the data.
                Defaults to None.
        """

        self.data = pd.read_csv(test_file)
        self.data = self.data.iloc[:, 1:]  # Select all columns except the first
        self.transform = transform

        if transform is not None:
            self.data = self.transform(np.array(self.data))

    def __len__(self):
        """
        Returns the length of the dataset (number of data points).

        Returns:
            int: Length of the dataset.
        """

        return len(self.data[0])

    def __getitem__(self, ind):
        """
        Retrieves a single data point from the dataset.

        Args:
            ind (int): Index of the data point to retrieve.

        Returns:
            tensor: A tensor representing the data point.
        """

        user_vector = self.data.values[0][ind]  # Access data using .values for efficiency

        return user_vector
