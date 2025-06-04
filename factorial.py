import math

def factorial_math(n):
  """Calculates the factorial of a number using the math.factorial() function."""
  if not isinstance(n, int) or n < 0:
    raise ValueError("Factorial is only defined for non-negative integers.")
  return math.factorial(n)

# Example usage
number = 5
result = factorial_math(number)
print(f"The factorial of {number} is {result}") # Output: The factorial of 5 is 120")
