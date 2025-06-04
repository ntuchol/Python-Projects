def find_largest_odd(numbers):
    """
    Finds the largest odd number in a list of integers.

    Args:
      numbers: A list of integers.

    Returns:
      The largest odd number in the list, or -1 if no odd number is found.
    """
    largest_odd = -1
    for number in numbers:
        if number % 2 != 0 and number > largest_odd:
            largest_odd = number
    return largest_odd