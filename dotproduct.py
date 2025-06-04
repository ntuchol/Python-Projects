def dot_product(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must be of the same length")
    return sum(x * y for x, y in zip(vector1, vector2))

# Example usage
vector_a = [1, 2, 3]
vector_b = [4, 5, 6]
result = dot_product(vector_a, vector_b)
print("Dot Product:", result)