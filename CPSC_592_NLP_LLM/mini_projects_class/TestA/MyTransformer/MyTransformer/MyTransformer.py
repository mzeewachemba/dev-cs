import sys
import torch
from einops import rearrange

class MyTransformer(torch.nn.Module):
    def __init__(self, d) - > None:
        super().__init__()
        # d is the dimension of the embedding
        self.qkv = torch.nn.Linear(d, 3*d)  #learns q, k, v simultaneously
        self.wo = torch.nn.Linear(d , d)  #learns the output wight dimension d * d

    def forward(self, x):
        myqkv = self.qkv(x)
        print(myqkv.shape) #torch.Size([4, 100, 1536])
        q,k,v = tuple(rearrange(myqkv, 'b n (d qkv) -> qkv b n d', qkv=3)) 

def main():
    #creating artificial data
    batch = 4
    x = torch.rand((batch, 100, 512))
    net = MyTransformer(512)
    out = net(x) 

if __name__ == "__main__":
    sys.exit(main())


