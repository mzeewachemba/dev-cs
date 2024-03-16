import sys
import numpy as np

def compute_svd(A):
    """
    Compute the Singular Value Decomposition (SVD) of matrix A and print intermediate results.

    Parameters:
    A (ndarray): Input matrix.

    Returns:
    None
    """
    # Compute the Singular Value Decomposition (SVD) of matrix A
    u, s, v = np.linalg.svd(A)
    
    # Print intermediate results
    print("----u----")
    print(u)
    
    print("----s----")
    # Convert singular values to a diagonal matrix
    s = np.diag(s)
    
    # Check if the number of columns in the diagonal matrix is less than the number of columns in A
    if s.shape[1] != A.shape[1]:
        # Stack zero columns in the diagonal matrix to match the shape of A
        num_zero_cols = A.shape[1] - s.shape[1]
        sz = np.zeros((s.shape[0], A.shape[1]))
        sz[:, :-1] = s  # Extra columns of zeros
        s = sz
    print(s)
    
    print("----v----")
    print(v)
    
    # Reconstruct the matrix A from its SVD components
    Asvd = np.dot(np.dot(u, s), v)
    print("----A from SVD components------")
    print(Asvd)

def main():
    # Compute Eigenvalues, Eigenvectors, SVD for [[3,1], [1,3]]
    Alist = [[3, 1], [1, 3]]
    A = np.asarray(Alist, dtype=float)  # Convert list to numpy array
    eigen_vals = np.linalg.eigvals(A)
    print("Eigenvalues:", eigen_vals)
    
    eigenvs, eigen_vecs = np.linalg.eig(A)
    print("Eigenvectors:")
    print(eigen_vecs)
    
    compute_svd(A)
    
    # Compute SVD of [[3,2,2], [2,3,-2]]
    print("-----------second example - SVD of 2x3 matrix")
    A2list = [[3, 2, 2], [2, 3, -2]]
    A2 = np.asarray(A2list, dtype=float)
    compute_svd(A2)

if __name__ == "__main__":
    sys.exit(int(main() or 0))
