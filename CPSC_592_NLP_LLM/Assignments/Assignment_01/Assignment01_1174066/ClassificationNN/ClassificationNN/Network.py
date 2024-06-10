import torch

class Network(torch.nn.Module):
    def __init__(self, hidden_size, output_size=2) -> None:
        super().__init__()
        self.fc1 = torch.nn.Linear(2, hidden_size)  # 2 inputs, hidden_size outputs
        self.fc2 = torch.nn.Linear(hidden_size, output_size)
        # self.act = torch.nn.ReLU() # ReLU activation function enable and disable
        self.act = None 
        self.sm = torch.nn.Softmax(dim=1)

    def forward(self, x):
        x = self.fc1(x)
        # x = self.act(x) # ReLU activation function enable and disable
        x = self.sm(self.fc2(x))
        return x
