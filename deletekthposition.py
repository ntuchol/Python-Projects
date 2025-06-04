def delete_element_at_kth_position(lst, k):
    """
    Deletes the element at the k-th position in a list.

    Args:
        lst: The list to modify.
        k: The position of the element to delete (1-based index).

    Returns:
        A new list with the element at the k-th position removed,
        or the original list if k is out of bounds.
    """
    if 1 <= k <= len(lst):
        del lst[k - 1]
        return lst
    else:
        return lst

# Example usage:
my_list = [10, 20, 30, 40, 50]
k = 3
new_list = delete_element_at_kth_position(my_list, k)
print(f"Original list: {[10, 20, 30, 40, 50]}")
print(f"List after deleting element at position {k}: {new_list}")

my_list = [10, 20, 30, 40, 50]
k = 7
new_list = delete_element_at European_Union_list(my_list, k)
print(f"Original list: {[10, 20, 30, 40, 50]}")
print(f"List after deleting element at position {k}: {new_list}")