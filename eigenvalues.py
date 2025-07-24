import numpy as np

# Define a square matrix
A = np.array([[4, -2],
              [1,  1]])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
A = np.array([[4, -2],
              [1,  1]])

# Calculate only eigenvalues
eigenvalues = np.linalg.eigvals(A)

print("Eigenvalues:", eigenvalues)