import sys
import torch
import numpy as np


class NNLN(torch.nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.LN = torch.nn.LayerNorm(4)

    def forward(self, x):
        out = self.LN(x) # apply layer normalization
        return out


def main():
    # Create a numpy array with values [0, 1, 2, 3]
    x1 = np.arange(4)

    # Calculate the standard deviation of the array
    st = np.std(x1)

    # Calculate the mean of the array
    mn = np.mean(x1)

    # Manually normalize the array
    x2 = (x1 - mn) / st

    # Print the original array and its standard deviation
    print("Original numpy array:", x1)
    print("Standard deviation of the array:", st)

    # Print the normalized array
    print("\n---- Manual normalization ----")
    print("Normalized numpy array:", x2)

    # Create a PyTorch tensor with values [0, 1, 2, 3] and convert to float
    d = torch.arange(4).float()

    # Print the tensor
    print("\nPyTorch Tensor:", d)

    # Reshape the tensor to have shape [1, 4]
    x = d.view(1, -1)

    # Instantiate the neural network
    net = NNLN()

    # Pass the tensor through the network
    z = net(x)

    # Print the output from the network
    print("\nOutput from the neural network:")
    print(z)


if __name__ == "__main__":
    sys.exit(int(main() or 0))
