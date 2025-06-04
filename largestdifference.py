def find_largest_difference(numbers):
    """
    Finds the largest difference between any two numbers in a list.

    Args:
        numbers: A list of numbers.

    Returns:
        The largest difference between any two numbers in the list.
        Returns 0 if the list is empty or has only one element.
    """
    if len(numbers) < 2:
        return 0
    
    min_num = min(numbers)
    max_num = max(numbers)
    return max_num - min_num

# Example usage:
numbers = [1, 5, 2, 9, 3]
largest_difference = find_largest_difference(numbers)
print(f"The largest difference is: {largest_difference}") # Output: 8

numbers2 = [-10, 5, 0, -3, 8]
largest_difference2 = find_largest_difference(numbers2)
print(f"The largest difference is: {largest_difference2}") # Output: 18