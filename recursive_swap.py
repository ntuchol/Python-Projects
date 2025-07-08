def recursive_swap(lst, index=0):
    """
    Recursively swaps adjacent elements in a list.

    Args:
        lst: The list to modify.
        index: The current starting index for swapping.
    """
    if index >= len(lst) - 1:
        return  # Base case: Stop recursion if end of list is reached

    # Swap elements at current index and next index
    lst[index], lst[index + 1] = lst[index + 1], lst[index]

    # Recursive call to process the rest of the list
    recursive_swap(lst, index + 2)

# Example usage
my_list = [1, 2, 3, 4, 5, 6]
recursive_swap(my_list)
print(my_list) # Output: [2, 1, 4, 3, 6, 5]
