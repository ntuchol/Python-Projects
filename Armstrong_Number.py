def is_armstrong_number(number):
    """
    Checks if a given number is an Armstrong number.
    """
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_powers = 0

    for digit_char in num_str:
        digit = int(digit_char)
        sum_of_powers += digit ** num_digits

    return sum_of_powers == number

# Test cases
print(f"Is 153 an Armstrong number? {is_armstrong_number(153)}")
print(f"Is 370 an Armstrong number? {is_armstrong_number(370)}")
print(f"Is 123 an Armstrong number? {is_armstrong_number(123)}")
print(f"Is 1634 an Armstrong number? {is_armstrong_number(1634)}")