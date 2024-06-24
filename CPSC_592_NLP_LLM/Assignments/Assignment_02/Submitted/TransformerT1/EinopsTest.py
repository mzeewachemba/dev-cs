import sys
import torch
from einops import rearrange


def main():
    A = torch.tensor([[1, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9, 10, 11, 12],
                      [13, 14, 15, 16]])
    print("\nPrinting tensor A:\n", A)

    B = torch.tensor([[1, 2, 1, 1],
                      [3, 4, 2, 5],
                      [1, 3, 6, 7],
                      [1, 4, 6, 8]])
    print("\nPrinting tensor B:\n", B)

    C = torch.einsum('ij, jk -> ik', A, B)  # matrix mult.
    print("\nPrinting matrix multiplication using Einstein summation:\n", C)

    C1 = torch.einsum('ij, jk -> ik', A, B)  # matrix mult.
    print("\nPrinting matrix multiplication Einstein summation C1:\n", C1)

    C2 = torch.einsum('ij, kj -> ik', A, B)  # Ax(transpose(B) - matrix mult.
    print("\nPrinting Ax(transpose(B) - matrix mult C2:\n", C2)

    At = torch.einsum('ij -> ji', A)  # transpose
    print("\nPrinting A transposed using Einstein summation:\n", At)

    C3 = torch.einsum("ii -> i", A)  # diagonal elements only, ii indicates the same rows and columns
    print("\nPrinting diagonal elements only C3:\n", C3)

    C4 = torch.einsum("ii -> ", A)  # sum diagonal elements - trace
    print("\nPrinting sum diagonal elements - trace C4:\n", C4)

    C5 = torch.einsum('ij -> j', A)  # sum column elements (row wise sum)
    print("\nPrinting sum column elements (row wise sum) C5:\n", C5)

    C6 = torch.einsum('ij, ij -> ij', A, B)  # element wise product
    print("\nPrinting element wise product C6:\n", C6)

    C7 = torch.einsum('ij, ij, ij -> ij', A, A, A)  # cube elements
    print("\nPrinting cube elements C7:\n", C7)

    C8 = torch.einsum('ij -> ji', A)  # transpose
    print("\nPrinting transpose C8:\n", C8)

    C9 = torch.einsum('ij,ij -> i', A, B)  # multiply row wise and add each row
    print("\nPrinting multiply row wise and add each row C9:\n", C9)

    d1 = torch.tensor([3, 5, 7, 9])
    d2 = torch.tensor([1, 2, 3, 4])
    douter = torch.einsum('i, j -> ij', d1, d2)  # outer product
    print("\nPrinting outer product douter:\n", douter)

    dinner = torch.einsum('i, i -> ', d1, d2)  # inner product
    print("\nPrinting inner product dinner:\n", dinner)

    dfrobenius = torch.einsum("ij, ij -> ", A, A)  # frobenius norm
    # sum of squares of all elements of a matrix
    print("\nPrinting frobenius norm...\n")
    print(dfrobenius)

    batch_tensor_1 = torch.arange(2 * 4 * 3).reshape(2, 4, 3)
    print("\nPrinting batch tensor 1 batch_tensor_1:\n", batch_tensor_1)

    batch_tensor_2 = torch.arange(2 * 4 * 3).reshape(2, 3, 4)
    print("\nPrinting batch tensor 2 batch_tensor_2:\n", batch_tensor_2)

    dmul = torch.einsum('bij, bjk -> bik', batch_tensor_1, batch_tensor_2)  # batch matrix multiplication
    print("\nPrinting batch matrix multiplication dmul:\n", dmul)

    dt = torch.randn((3, 5, 4, 6, 8, 2, 7, 9))  # 8 dimensions
    print("\nPrinting tensor shape dt:\n", dt.shape)

    esum = torch.einsum("ijklmnop -> p", dt)
    # marginalize or sum over dim p
    print("\nPrinting esum - sum over dim p:\n", esum)  #

    kv = torch.zeros((2, 1024, 64))  # 2 is batch size
    q = torch.zeros((2, 1024, 64))
    q2 = rearrange(q, 'b (n s) e->b n s e', s=16)
    print(f"Printing q2 shape: {q2.shape}")  # [2,64,16,64]

    q3 = rearrange(q2, 'b n s e-> (b n) s e')
    print(f"Printing q3 shape: {q3.shape}")  # [128,16,64]

if __name__ == "__main__":
    sys.exit(int(main() or 0))
