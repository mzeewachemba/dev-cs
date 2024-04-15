import torch
import torch.nn as nn
from torch.autograd import Variable


class MSELoss_with_Mask(nn.Module):
    def __init__(self):
        """
        Initializes an MSELoss_with_Mask module.

        This custom loss function calculates the mean squared error (MSE)
        considering a mask to exclude unrated items.
        """
        super(MSELoss_with_Mask, self).__init__()

    def forward(self, inputs, targets):
        """
        Calculates the MSE loss with masking.

        Args:
            inputs (torch.Tensor): Predicted ratings.
            targets (torch.Tensor): Ground truth ratings.

        Returns:
            torch.Tensor: The calculated MSE loss.
        """

        # Masking into a vector of 1's and 0's.
        mask = (targets != 0)
        mask = mask.float()

        # Actual number of ratings.
        # Take max to avoid division by zero while calculating loss.
        other = torch.Tensor([1.0])
        other = other.cuda()
        number_ratings = torch.max(torch.sum(mask), other)

        # Calculate squared error considering the mask
        error = torch.sum(torch.mul(mask, torch.mul((targets - inputs), (targets - inputs))))

        # Calculate loss as the mean squared error with masking
        loss = error.div(number_ratings)

        return loss[0]
