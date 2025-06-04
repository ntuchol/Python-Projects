def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Input from user
num = int(input("Enter a number: "))
result = factorial_iterative(num)
print(f"The factorial of {num} is {result}")