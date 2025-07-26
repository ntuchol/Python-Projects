def find_smallest(numbers):
    if not numbers:
        return None
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))
    numbers = []
    for i in range(n):
        num = int(input(f"Enter element {i+1}: "))
        numbers.append(num)
    
    smallest_number = find_smallest(numbers)
    if smallest_number is not None:
        print("The smallest element is:", smallest_number)
    else:
        print("No numbers were entered.")
