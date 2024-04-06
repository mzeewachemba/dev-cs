import torch
import sys
import torch.nn as nn
import torchvision

# CNN network followed by a with one hidden layer classifier
class Network(nn.Module):
    def __init__(self, hidden_size1, num_classes):
        super(Network, self).__init__()
        # self.conv1 = nn.Conv1d(1, 6, 15)  # 15x1 conv.kernel
        self.conv1 = nn.Conv1d(1, 16, 15)  # 16 feature maps
        # in_channels = 1 because of linear data
        self.relu = nn.ReLU()
        # self.conv2 = nn.Conv1d(6, 4, 18)
        self.conv2 = nn.Conv1d(16, 4, 18)
        # 20500 comes from the dimension of the last conv layer
        self.fc1 = nn.Linear(4 * 20500, hidden_size1)
        self.fc2 = nn.Linear(hidden_size1, num_classes)
        self.smax = nn.Softmax(dim=1)

    def forward(self, x):
        out = self.conv1(x)
        out = self.relu(self.conv2(self.relu(out)))
        flatten = out.view(-1, 4 * 20500)
        out = self.fc1(flatten)
        out = self.relu(out)
        out = self.fc2(out)
        out = self.smax(out)
        return out

