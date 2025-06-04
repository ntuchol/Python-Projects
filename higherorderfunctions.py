def apply_operation(func, items):
  """Applies a function to each item in an iterable."""
  return [func(item) for item in items]

def multiply_by(factor):
  """Returns a function that multiplies its argument by a factor."""
  def multiplier(x):
    return x * factor
  return multiplier

numbers = [1, 2, 3, 4, 5]

# Using apply_operation with a lambda function
squared_numbers = apply_operation(lambda x: x**2, numbers)
print(f"Squared numbers: {squared_numbers}")

# Using apply_operation with a defined function
def add_one(x):
  return x + 1
incremented_numbers = apply_operation(add_one, numbers)
print(f"Incremented numbers: {incremented_numbers}")

# Using multiply_by to create a custom function
double = multiply_by(2)
tripple = multiply_by(3)
print(f"Doubled numbers: {[double(x) for x in numbers]}")
print(f"Tripled numbers: {[tripple(x) for x in numbers]}")