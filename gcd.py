import math

# Calculate the GCD of two integers
num1 = 54
num2 = 24
gcd_value = math.gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {gcd_value}")

# Calculate the GCD of more than two integers
num3 = 108
num4 = 216
gcd_value_multiple = math.gcd(num1, num3, num4)
print(f"The GCD of {num1}, {num3}, and {num4} is: {gcd_value_multiple}")

# GCD with zero
num5 = 0
gcd_with_zero = math.gcd(num1, num5)
print(f"The GCD of {num1} and {num5} is: {gcd_with_zero}")