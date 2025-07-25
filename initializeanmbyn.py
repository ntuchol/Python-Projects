def initialize_empty_string_matrix(n, m):
    matrix = [['' for _ in range(m)] for _ in range(n)]
    return matrix

n = 3
m = 4
empty_string_matrix = initialize_empty_string_matrix(n, m)
print(empty_string_matrix)
