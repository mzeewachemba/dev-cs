import torch

class SimpleModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.w = torch.nn.Parameter(torch.randn(1, requires_grad=True, dtype=torch.float)) #requires_grad=True indicates to pytorch, that it should compute the gradients of the loss with respect to the w and the b parameters.
        self.b = torch.nn.Parameter(torch.randn(1, requires_grad=True, dtype=torch.float))

    def forward(self, x):
        return self.w * x + self.b

