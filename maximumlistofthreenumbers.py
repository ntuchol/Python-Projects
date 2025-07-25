def find_max_three(numbers):
    if len(numbers) < 3:
        return "List must contain at least three numbers"
    
    max1 = numbers[0]
    max2 = numbers[1]
    max3 = numbers[2]

    if max2 > max1:
        max1, max2 = max2, max1
    if max3 > max1:
        max1, max3 = max1, max3
    if max3 > max2:
        max2, max3 = max3, max2
    
    return [max1, max2, max3]

numbers_list = [10, 5, 8, 20, 15]
max_three = find_max_three(numbers_list)

print(f"The three largest numbers are: {max_three}") 
