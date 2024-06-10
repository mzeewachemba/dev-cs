import sys
import numpy as np
import torch

def main():
    # Create a tensor of zeros with shape (4,2,3)
    t1 = torch.zeros((4,2,3))
    print(f"\n t1.shape: {t1.shape}\n") # try t1.shape[0], t1.shape[1], t1.shape[2], t1,shape[-1]
    print(f"\n t1.shape[0]: {t1.shape[0]}\n") # try t1.shape[0]
    print(f"\n t1.shape[1]: {t1.shape[1]}\n") # try t1.shape[1]
    print(f"\n t1.shape[2]: {t1.shape[2]}\n") # try t1.shape[2]
    print(f"\n t1.shape[-1]: {t1.shape[-1]}\n") # try t1.shape[-1]
    
    # To add an extra dimension in the beginning i.e., to make the shape(1,4,2,3)
    t2 = t1.reshape(-1,4,2,3)
    print(f"\n Adding extra dim to t1: {t2.shape}\n")

    # To add an extra dimension in the beginning i.e., to make the shape(1,4,2,3)
    t3 = t1.view(-1,4,2,3)
    print(f"\n Adding extra dim to t1 using view: {t3.shape}\n")

    # To add a dimension at the end
    t4 = t1.view(4,2,3,-1)
    print(f"\n Adding extra dim at the end: {t4.shape}\n")

    # To add a dimension in the beginning using unsqueeze
    t5 = t1.unsqueeze(dim=0)
    print(f"\n Adding extra dim using unsqueeze: {t5.shape}\n")

    # Remove the added dimension using squeeze
    t6 = t5.squeeze(dim=0)
    print(f"\n Removing extra dim using squeeze: {t6.shape}\n")

    # Reshape while keeping the total number of elements same
    t7 = t1.reshape(4,6)
    print(f"\n Reshaping t1 to (4,6): {t7.shape}\n")
    
    # Use -1 to automatically infer the remaining dimension size
    t8 = t1.reshape(4,-1) # -1 will become 6 as t1 has 24 elements
    print(f"\n Reshaping t1 to (4,-1): {t8.shape}\n")

    # Unpack a tuple or a list using *
    aa = [(2,3,5),(6,7,8)]
    print(f'\n Unpacked list: {aa}\n') # unpacks the above list aa as two tuples
    
    # Zip operation to combine two tuples or lists
    bb, cc, dd = zip(*aa) # zip(*aa)=((2,6), (3,7), (5,8)), bb=(2,6)
    print(f'\n bb: {bb}\n')

    # Convert numpy array to tensor and add an extra dimension using None
    a = np.array([[5,3],[6,7]])
    b = torch.tensor(a, dtype=torch.int64)[None] # like unsqueeze, adds dimension
    print(f'\n After None shape: {b.shape}\n')

    # Gather allows us to select some elements from a tensor
    t = torch.tensor([[1,2],[3,4]]) # dim=1 selects by column
    r = torch.gather(t, dim=1, index=torch.tensor([[1,0],[0,1]]))
    print(f'\n r: {r}\n')

    # View to create a 1-d tensor
    w = t.view(-1) # will create 1-d tensor
    print(f'\n w: {w}\n')
    
    # View to create a 2-d tensor with one column
    v = t.view(-1)[:, None]
    print(f'\n v: {v.shape}\n') # 4x1

    # Gather along dimension 0
    r2 = torch.gather(t, dim=0, index=torch.tensor([[1,0],[0,1]]))
    print(f'\n r2: {r2}\n') # dim=0, selects row wise, r2=[[3,2][1,4]]

    # Gather along dimension 0
    r3 = torch.gather(t, dim=0, index=torch.tensor([[1],[0]]))
    print(f'\n r3: {r3}\n') # dim=0, selects row wise, r2=[[3],[1]]

    # Initialize a tensor
    out1 = torch.tensor([
        [0.10, 0.50, 0.40],  # correct
        [0.55, 0.20, 0.25],  # wrong
        [0.60, 0.10, 0.30],  # correct
        [0.15, 0.65, 0.20]   # correct
    ])
    print(f'\n out1: {out1.shape}\n')  # [4,3]

    # Target indices
    y = torch.tensor([1, 2, 0, 1], dtype=torch.int64)  # indices, can vary 0-2
    y = y.reshape(4, 1)  # to match out1
    probs = out1.gather(dim=1, index=y)  # dim=1, selects index on each row
    print(f'\n Probs using gather with y: {probs}\n')

    # 2D target indices
    y2 = torch.tensor([[1, 1], [2, 0], [0, 1], [1, 2]], dtype=torch.int64)  # targets
    probs2 = out1.gather(dim=1, index=y2)
    print(f'\n Probs2 using gather with y2: {probs2}\n')

    # Compute mean along a dimension
    out1_mean = out1.mean(dim=1, keepdim=True)  # keepdim, makes the output 4x1
    print(f'\n Mean along dim 1: {out1_mean}\n')

    # Masking
    state = torch.tensor([[0, 0, 0], [0, 0, 0], [0, 0, 1]])
    mask = ~(state != 0)  # 0 cells will be True, 1 cells will be False
    print(f'\n Mask with True for 0 and False for non-zero: {mask}\n')
    
    mask = ~(state != 0) * 1  # True cells will be 1, False will be 0
    print(f'\n Mask with 1 for True and 0 for False: {mask}\n')
    
    mask2 = (state != 0) * -1000  # non zero cells will become -1000
    print(f'\n Mask with -1000 for non-zero: {mask2}\n')
    
    mask3 = (state > 0).float()
    print(f'\n Mask with float values (1.0 for > 0): {mask3}\n')

    # Use np.eye for one-hot encoding
    board = [0, 0, 1, 0, 2, 0, 1, 2, 0]  # example board state
    print(f'\n np.eye(3): {np.eye(3)}\n')
    print(f'\n One-hot encoded board: {np.eye(3)[board]}\n')  # eye is diagonal matrix, select rows by board
    print('---------')
    print(f'\n Switching 2nd and 3rd column in one-hot encoded board: {np.eye(3)[board][:, [0, 2, 1]]}\n')  # switch 2nd and 3rd column

if __name__ == "__main__":
    sys.exit(int(main() or 0))
