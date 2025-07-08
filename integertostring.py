def int_to_base_string(number, base):
    """
    Converts an integer to a string representation in a specified base.

    Args:
        number (int): The integer to convert.
        base (int): The target base (e.g., 2 for binary, 10 for decimal, 16 for hexadecimal).

    Returns:
        str: The string representation of the number in the given base.
    """
    if not (2 <= base <= 36):  # Common range for bases using digits and letters
        raise ValueError("Base must be between 2 and 36.")

    if number == 0:
        return "0"

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    is_negative = False

    if number < 0:
        is_negative = True
        number = abs(number)

    while number > 0:
        remainder = number % base
        result.append(digits[remainder])
        number //= base  # Integer division

    if is_negative:
        result.append("-")

    return "".join(result[::-1])  # Reverse the list and join to form the string