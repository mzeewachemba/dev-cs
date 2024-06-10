import torch
import torch.nn as nn
import torch.nn.functional as F


class NetworkCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 32, 5)  # Input is color image with 3 channels
        self.pool = nn.MaxPool2d(2, 2)  # Maxpool defined once

        self.conv2 = nn.Conv2d(32, 6, 5)  # 53x53 comes from the last conv layer dimension

        # Assuming the input image size is 224x224 after convolutions and pooling
        self.fc1 = nn.Linear(6 * 53 * 53, 100)
        self.fc2 = nn.Linear(100, 3)
        self.sm = nn.Softmax(dim=1)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 6 * 53 * 53)  # Flatten the input
        x = F.relu(self.fc1(x))
        x = self.sm(self.fc2(x))  # Softmax activation on the final layer
        return x

