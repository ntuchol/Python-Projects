def apply_operation(func, items):
  return [func(item) for item in items]

def multiply_by(factor):
  def multiplier(x):
    return x * factor
  return multiplier

numbers = [1, 2, 3, 4, 5]

squared_numbers = apply_operation(lambda x: x**2, numbers)
print(f"Squared numbers: {squared_numbers}")

def add_one(x):
  return x + 1
incremented_numbers = apply_operation(add_one, numbers)
print(f"Incremented numbers: {incremented_numbers}")

double = multiply_by(2)
tripple = multiply_by(3)
print(f"Doubled numbers: {[double(x) for x in numbers]}")
print(f"Tripled numbers: {[tripple(x) for x in numbers]}")
