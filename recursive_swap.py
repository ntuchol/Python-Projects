def recursive_swap(lst, index=0):
    
    if index >= len(lst) - 1:
        return  
    lst[index], lst[index + 1] = lst[index + 1], lst[index]

    recursive_swap(lst, index + 2)

my_list = [1, 2, 3, 4, 5, 6]
recursive_swap(my_list)
print(my_list) 
