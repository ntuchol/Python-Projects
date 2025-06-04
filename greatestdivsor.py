def greatest_divisor(n):
    # Start checking from n//2 down to 1
    for i in range(n // 2, 0, -1):
        if n % i == 0:
            return i

# Example usage
number = 100
print(f"The greatest divisor of {number} (other than itself) is {greatest_divisor(number)}.")