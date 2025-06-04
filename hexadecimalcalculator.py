

def hex_calculator():
    print("Hexadecimal Calculator")
    print("Choose an operation: +, -, *, /")
    operation = input("Enter operation: ")

    if operation not in ['+', '-', '*', '/']:
        print("Invalid operation. Please choose +, -, *, or /.")
        return

    hex1 = input("Enter the first hexadecimal number (e.g., 1A): ").strip()
    hex2 = input("Enter the second hexadecimal number (e.g., 2F): ").strip()

    try:
        # Convert hexadecimal to integers
        num1 = int(hex1, 16)
        num2 = int(hex2, 16)

        # Perform the chosen operation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 // num2  # Integer division

        # Convert the result back to hexadecimal
        print(f"Result in hexadecimal: {hex(result).upper()[2:]}")
    except ValueError:
        print("Invalid hexadecimal input. Please try again.")

# Run the calculator
hex_calculator()