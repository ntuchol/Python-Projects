import math

def is_prime_wilson(n):
    if n <= 1:
        return False
    return (math.factorial(n - 1) + 1) % n == 0

print(is_prime_wilson(7))  
print(is_prime_wilson(9))  
