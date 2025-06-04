from collections import Counter

def element_frequency(arr):
    """
    Calculates the frequency of each element in an array.

    Args:
        arr: The input array (list).

    Returns:
        A dictionary where keys are the elements and values are their frequencies.
    """
    return Counter(arr)

# Example usage:
my_array = [1, 2, 2, 3, 1, 4, 1]
frequencies = element_frequency(my_array)
print(frequencies)
# Expected output: Counter({1: 3, 2: 2, 3: 1, 4: 1})