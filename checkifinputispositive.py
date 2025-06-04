def is_positive(num):
  """Checks if a number is positive.

  Args:
    num: The number to check.

  Returns:
    True if the number is positive, False otherwise.
  """
  return num > 0

# Example usage
user_input = input("Enter a number: ")
try:
  number = float(user_input)
  if is_positive(number):
    print(f"{number} is a positive number.")
  else:
    print(f"{number} is not a positive number.")
except ValueError:
  print("Invalid input. Please enter a valid number.")