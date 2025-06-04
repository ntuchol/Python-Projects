# Method 1: Direct initialization
octal_list_direct = [0o10, 0o20, 0o30, 0o40]
print(octal_list_direct)
# Output: [8, 16, 24, 32]

# Method 2: Using a loop and the oct() function
decimal_numbers = [8, 16, 24, 32]
octal_list_loop = []
for num in decimal_numbers:
    octal_list_loop.append(oct(num))
print(octal_list_loop)
# Output: ['0o10', '0o20', '0o30', '0o40']

# Method 3: List comprehension with oct()
decimal_numbers = [8, 16, 24, 32]
octal_list_comprehension = [oct(num) for num in decimal_numbers]
print(octal_list_comprehension)
# Output: ['0o10', '0o20', '0o30', '0o40']
            current = current.next