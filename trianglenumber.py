import math

def is_triangle_number(num):
    if num < 1:
        return False
    # Solve the quadratic equation n^2 + n - 2*num = 0
    n = (-1 + math.sqrt(1 + 8 * num)) / 2
    return n.is_integer()

# Example usage
number = 15
print(f"Is {number} a triangle number? {is_triangle_number(number)}")
