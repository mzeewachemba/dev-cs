import sys
import torch
from torch import nn
from einops import rearrange


class TransformerLayer(nn.Module):
    def __init__(self, d) -> None:
        super().__init__()

        self.qkv = nn.Linear(d, d * 3)
        self.wo = nn.Linear(d, d)

    def forward(self, x):
        x = self.qkv(x)
        q, k, v = tuple(rearrange(x, 'b n (k d h)->k b h n d', k=3, h=8))
        attn = torch.einsum('b h i k, b h j k->b h i j', q, k) # multiply q and k transpose
        out = torch.einsum('b h i k, b h k j->b h i j', attn, v) # multiply attn and v normal multiplication
        out = rearrange(out, 'b h n d->b n (h d)')
        out = self.wo(out)
        return out


def main():
    net = TransformerLayer(512)
    x = torch.rand((4, 100, 512))
    z = net(x)
    print(z.shape)

    # Example tensor with shape [2, 4, 3, 5]
    out = torch.randn(2, 4, 3, 5)

    # Rearrange the tensor
    out = rearrange(out, 'b h n d -> b n (h d)')

    # Print the new shape
    print(out.shape)  # Output: torch.Size([2, 3, 20])


if __name__ == "__main__":
    sys.exit(int(main() or 0))
