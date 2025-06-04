def print_multiplication_table(size):
    # Print the header row
    print("   ", end="")
    for i in range(1, size + 1):
        print(f"{i:4}", end="")
    print("\n" + "----" * (size + 1))

    # Print each row of the multiplication table
    for i in range(1, size + 1):
        print(f"{i:2} |", end="")
        for j in range(1, size + 1):
            print(f"{i * j:4}", end="")
        print()

# Customize the size of the multiplication table here
table_size = 10
print_multiplication_table(table_size)