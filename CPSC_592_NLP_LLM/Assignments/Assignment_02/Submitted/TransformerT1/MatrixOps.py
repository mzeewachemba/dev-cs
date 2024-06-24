import torch
import sys
import numpy


def main():
    a = torch.arange(2 * 2).reshape(2, 2)
    print("\nPrinting tensor a:\n", a)

    b = torch.arange(2 * 2).reshape(2, 2)
    print("\nPrinting tensor b:\n", b)

    c = a * b
    print("\nPrinting element by element multiplication:\n", c)

    d = a + b
    print("\nPrinting matrix addition:", d)

    e = torch.arange(2 * 3).reshape(2, 3)
    print("\nPrinting tensor e , 2 rows and 3 columns values ranging from 0 to 5:\n", e)

    f = torch.matmul(a, e)
    print("\nPrinting matrix multiplication:", f)

    f1 = a @ e
    print("\nPrinting matrix multiplication (alternative syntax):\n", f1)

    g = torch.transpose(f, 0, 1)
    print("\nPrinting transpose, dim swapped:\n", g)

    f1 = torch.unsqueeze(f, dim=0)
    print(f"\nPrinting tensor f with an added dimension in the beginning: \n{f1.shape} \nf1 is: {f1}")

    # Create a 2x2x3 matrix with specific values
    v = [[[1, 2, 3], [4, 5, 6]],
              [[7, 8, 9], [10, 11, 12]]]
    x = torch.tensor(v)
    print(f"\nPrinting 2x2x3 tensor matrix:\n {x} and \nsize: {x.size()}")

    f1t = torch.transpose(f1, 1, 2)
    print("\nPrinting transpose with the added dimension:\n", f1t)

    tensor1 = torch.randn(10, 3, 4)
    tensor2 = torch.randn(10, 4, 5)
    res = torch.matmul(tensor1, tensor2)
    print("\nPrinting batch matrix multiplication: \n", res.shape)

    y = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"\nPrinting tensor y:\n {y} and \nsize: {y.size()}")

    z = torch.full((2, 2), 5)
    print("\nPrinting tensor z:\n", z)

if __name__ == "__main__":
    sys.exit(int(main() or 0))
