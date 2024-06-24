import sys
import torch
import numpy as np


def main():
    i = 4
    j = 4

    # Create a mask of size (i, j) with ones on the upper triangle (including the diagonal) and convert to boolean
    mask = torch.ones(i, j, device=None).triu_(0).bool()  # try with triu_(0)

    # Print the created mask
    print("Mask with upper triangle filled with ones and converted to boolean:")
    print(mask)
    print('\n')

    # Create a random (4, 4) attention matrix on the CPU
    attn = torch.rand((4, 4)).cpu()

    # Print the random attention matrix
    print("Random attention matrix (4x4) on CPU:")
    print(attn)
    print('\n')

    # Apply the mask to the attention matrix, setting masked positions to -infinity
    attn_masked = attn.masked_fill(mask, -np.inf)

    # Print the masked attention matrix
    print("Attention matrix after applying the mask (masked positions set to -infinity):")
    print(attn_masked)


if __name__ == "__main__":
    sys.exit(int(main() or 0))
