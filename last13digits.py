number = 12345678901234567890
last_13_digits = number % (10**13)
print(last_13_digits)
# Expected Output: 2345678901234

number = 12345
last_13_digits = number % (10**13)
print(last_13_digits)
# Expected Output: 12345