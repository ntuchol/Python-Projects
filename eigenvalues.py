import numpy as np

A = np.array([[4, -2],
              [1,  1]])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
A = np.array([[4, -2],
              [1,  1]])

eigenvalues = np.linalg.eigvals(A)

print("Eigenvalues:", eigenvalues)
