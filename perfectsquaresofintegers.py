# Generate perfect squares of integers up to a given limit
def perfect_squares(limit):
    return [i**2 for i in range(1, limit + 1)]

# Example usage
limit = 10  # Adjust the limit as needed
squares = perfect_squares(limit)
print(squares)