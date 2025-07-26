octal_list_direct = [0o10, 0o20, 0o30, 0o40]
print(octal_list_direct)

decimal_numbers = [8, 16, 24, 32]
octal_list_loop = []
for num in decimal_numbers:
    octal_list_loop.append(oct(num))
print(octal_list_loop)

decimal_numbers = [8, 16, 24, 32]
octal_list_comprehension = [oct(num) for num in decimal_numbers]
print(octal_list_comprehension)
            current = current.next
