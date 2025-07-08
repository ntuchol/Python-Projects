my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)

def square_number(num):
  """Calculates the square of a given number."""
  return num * num

numbers = [1, 2, 3, 4, 5]

# Use map() with the defined square_number function
squared_numbers_map_object = map(square_number, numbers)

# Convert the map object to a list to view the results
squared_numbers_list = list(squared_numbers_map_object)

print(f"Original list: {numbers}")
print(f"Squared elements (using map and defined function): {squared_numbers_list}")