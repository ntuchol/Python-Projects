def count_digits_recursive(input_string):
    if not input_string:
        return 0
    elif '0' <= input_string[0] <= '9':
        return 1 + count_digits_recursive(input_string[1:])
    else:
         return count_digits_recursive(input_string[1:])

# Example Usage
string_example = "abc123def45"
digit_count = count_digits_recursive(string_example)
print(f"The number of digits in the string is: {digit_count}") # Output: The number of digits in the string is: 5