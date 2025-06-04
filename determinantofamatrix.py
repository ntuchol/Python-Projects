import numpy as np

# Define a square matrix as a NumPy array
matrix = np.array([[1, 2], [3, 4]])

# Calculate the determinant using numpy.linalg.det()
determinant = np.linalg.det(matrix)

# Print the determinant
print("Determinant:", determinant)