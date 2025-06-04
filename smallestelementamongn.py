def find_smallest(numbers):
    """
    Finds the smallest element in a list of numbers.

    Args:
      numbers: A list of numbers.

    Returns:
      The smallest number in the list, or None if the list is empty.
    """
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