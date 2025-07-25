def generate_natural_numbers(n):
  
  if not isinstance(n, int) or n <= 0:
    raise ValueError("Input must be a positive integer.")
  return list(range(1, n + 1))

num_elements = 10
natural_numbers_list = generate_natural_numbers(num_elements)
print(natural_numbers_list) 

num_elements = 5
natural_numbers_list = generate_natural_numbers(num_elements)
print(natural_numbers_list) 
