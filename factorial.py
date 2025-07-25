import math

def factorial_math(n):
  if not isinstance(n, int) or n < 0:
    raise ValueError("Factorial is only defined for non-negative integers.")
  return math.factorial(n)

number = 5
result = factorial_math(number)
print(f"The factorial of {number} is {result}") 
