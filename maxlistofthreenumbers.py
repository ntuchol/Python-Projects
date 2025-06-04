def find_max_of_three(a, b, c):
    # Compare the first two numbers
    if a > b:
        if a > c:
            return a  # a is the largest
        else:
            return c  # c is the largest
    else:
        if b > c:
            return b  # b is the largest
        else:
            return c  # c is the largest

# Example usage
numbers = [5, 12, 9]
result = find_max_of_three(numbers[0], numbers[1], numbers[2])
print("The maximum number is:", result)
