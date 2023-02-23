import numpy as np
M=np.array([[2,1,1],[2,3,2],[1,1,2]])
eigenvalues, eigenvectors= np.linalg.eig(M)
if np.all(np.isreal(eigenvalues)) and np.linalg.matrix_rank(eigenvectors)==M.shape[0]:
    print("the matrix is diagonalizable.")
else:
    print("the matrix is not diagonalizable.")

print("eigenvalues")
print(eigenvalues)
print("eigenvector matrix")
print(eigenvectors)