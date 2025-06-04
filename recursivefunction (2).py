def factorial(n):
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:  # Recursive case: n! = n * (n-1)!
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120
    