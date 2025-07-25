def find_largest_difference(numbers):
    if len(numbers) < 2:
        return 0
    
    min_num = min(numbers)
    max_num = max(numbers)
    return max_num - min_num

numbers = [1, 5, 2, 9, 3]
largest_difference = find_largest_difference(numbers)
print(f"The largest difference is: {largest_difference}") 

numbers2 = [-10, 5, 0, -3, 8]
largest_difference2 = find_largest_difference(numbers2)
print(f"The largest difference is: {largest_difference2}") 
