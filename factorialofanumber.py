# Iterative approach
def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Recursive approach
def factorial_recursive(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Example usage
number = 5
print(f"Factorial of {number} (iterative): {factorial_iterative(number)}")
print(f"Factorial of {number} (recursive): {factorial_recursive(number)}")

number = 0
print(f"Factorial of {number} (iterative): {factorial_iterative(number)}")
print(f"Factorial of {number} (recursive): {factorial_recursive(number)}")

number = -1
print(f"Factorial of {number} (iterative): {factorial_iterative(number)}")
print(f"Factorial of {number} (recursive): {factorial_recursive(number)}")