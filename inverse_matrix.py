import numpy as np

matrix_a = np.array([[1, 2, 3, 4, 5],
                     [6, 7, 8, 9, 10],
                     [11, 12, 13, 14, 15],
                     [16, 17, 18, 19, 20],
                     [21, 22, 23, 24, 25]])

try:
    matrix_a_inv = np.linalg.inv(matrix_a)
    print("The inverse of matrix A is:\n", matrix_a_inv)
except np.linalg.LinAlgError:
    print("Matrix A is singular and does not have an inverse.")

identity_matrix = np.dot(matrix_a, matrix_a_inv)
print("\nResult of A * A_inv:\n", identity_matrix)
