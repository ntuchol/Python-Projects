def reverse_array(arr):
    """Reverses the order of elements in an array.

    Args:
        arr: The array (list) to be reversed.

    Returns:
        A new array with elements in reversed order.
    """
    return arr[::-1]

# Example usage:
my_array = [1, 2, 3, 4, 5]
reversed_array = reverse_array(my_array)
print(reversed_array)  # Output: [5, 4, 3, 2, 1]