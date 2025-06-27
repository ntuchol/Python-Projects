import math

result = math.factorial(5)
print(result)  # Output: 120

def factorial_iterative(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

result = factorial_iterative(5)
print(result)  # Output: 120

def factorial_recursive(n):
    if n < 2:
        return 1
    else:
        return n * factorial_recursive(n - 1)

result = factorial_recursive(5)
print(result) # Output: 120