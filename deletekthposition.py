def delete_element_at_kth_position(lst, k):
    
    if 1 <= k <= len(lst):
        del lst[k - 1]
        return lst
    else:
        return lst


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
