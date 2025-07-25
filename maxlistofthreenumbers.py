def find_max_of_three(a, b, c):
    if a > b:
        if a > c:
            return a  
        else:
            return c  
    else:
        if b > c:
            return b  
        else:
            return c  
            
numbers = [5, 12, 9]
result = find_max_of_three(numbers[0], numbers[1], numbers[2])
print("The maximum number is:", result)
