def generate_natural_numbers(n):
  """
  Generates a list containing the first n natural numbers.

  Args:
    n: An integer representing the number of natural numbers to generate.

  Returns:
    A list of integers from 1 to n.
  """
  if not isinstance(n, int) or n <= 0:
    raise ValueError("Input must be a positive integer.")
  return list(range(1, n + 1))

# Example usage:
num_elements = 10
natural_numbers_list = generate_natural_numbers(num_elements)
print(natural_numbers_list) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num_elements = 5
natural_numbers_list = generate_natural_numbers(num_elements)
print(natural_numbers_list) # Output: [1, 2, 3, 4, 5]