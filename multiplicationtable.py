def print_multiplication_table(size):
    print("   ", end="")
    for i in range(1, size + 1):
        print(f"{i:4}", end="")
    print("\n" + "----" * (size + 1))

    for i in range(1, size + 1):
        print(f"{i:2} |", end="")
        for j in range(1, size + 1):
            print(f"{i * j:4}", end="")
        print()

table_size = 10
print_multiplication_table(table_size)
