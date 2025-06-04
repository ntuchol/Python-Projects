def sum_of_diagonals(matrix):
    """
    Calculates the sum of the diagonal elements of a square matrix.

    Args:
      matrix: A list of lists representing the square matrix.

    Returns:
      The sum of the diagonal elements.
    """
    n = len(matrix)
    diagonal_sum = 0
    for i in range(n):
        diagonal_sum += matrix[i][i]  # Add element at matrix[i][i] which are diagonal elements

    return diagonal_sum

# Example usage:
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
print(f"Sum of diagonals for matrix1: {sum_of_diagonals(matrix1)}")  # Output: 15

matrix2 = [[10, 11, 12, 13],
           [14, 15, 16, 17],
           [18, 19, 20, 21],
           [22, 23, 24, 25]]
print(f"Sum of diagonals for matrix2: {sum_of_diagonals(matrix2)}")  # Output: 70