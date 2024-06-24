import sys
import torch
import torch.nn.functional as F


def main():
    # Create a tensor of logits (raw predictions before applying softmax)
    logits = torch.tensor([1, 2, 3, 1, 3, 2, 3], dtype=torch.float)

    # Apply softmax to logits to get probabilities
    s = F.softmax(logits, dim=0)

    # Simulate top-k selection by zeroing out certain entries
    s[1] = 0
    s[6] = 0

    # Print the modified softmax probabilities
    print("Softmax probabilities after zeroing out some entries:")
    print(s)

    # Use torch.multinomial to sample one index probabilistically based on the softmax probabilities
    index1 = torch.multinomial(s, 1)  # returns index of one top choice based on probabilities
    print("\nIndex of one top choice (sampled probabilistically):")
    print(index1)

    # Use torch.multinomial to sample two indices probabilistically based on the softmax probabilities
    index2 = torch.multinomial(s, 2)  # returns indices of top 2 choices based on probabilities
    print("\nIndices of top 2 choices (sampled probabilistically):")
    print(index2)

    # Use torch.multinomial to sample two indices probabilistically based on the softmax probabilities
    index3 = torch.multinomial(s, 3)  # returns indices of top 3 choices based on probabilities
    print("\nIndices of top 3 choices (sampled probabilistically):")
    print(index3)


if __name__ == "__main__":
    sys.exit(int(main() or 0))
