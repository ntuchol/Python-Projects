def check_even_odd(number):
  """
    Checks if a number is even or odd.

    Args:
      number: The number to check.

    Returns:
      "Even" if the number is even, "Odd" if the number is odd.
  """
  if number % 2 == 0:
    return "Even"
  else:
    return "Odd"

# Get input from the user
num = int(input("Enter an integer: "))

# Check if the number is even or odd and print the result
result = check_even_odd(num)
print(f"{num} is {result}")