def initialize_empty_string_matrix(n, m):
    """
    Initializes an n-by-m list of lists with empty strings.

    Args:
        n: The number of rows.
        m: The number of columns.

    Returns:
        A list of lists representing the n-by-m matrix, where each element is an empty string.
    """
    matrix = [['' for _ in range(m)] for _ in range(n)]
    return matrix

# Example usage:
n = 3
m = 4
empty_string_matrix = initialize_empty_string_matrix(n, m)
print(empty_string_matrix)