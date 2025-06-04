def find_second_highest(numbers):
    if len(numbers) < 2:
        return "Not enough numbers to find second highest."

    unique_numbers = sorted(list(set(numbers)), reverse=True)

    if len(unique_numbers) < 2:
         return "Not enough unique numbers to find second highest."
    
    return unique_numbers[1]

if __name__ == "__main__":
    try:
        n = int(input("Enter the number of elements: "))
        if n <= 0:
            print("Please enter a positive number of elements.")
        else:
            numbers = []
            for i in range(n):
                num = int(input(f"Enter element {i+1}: "))
                numbers.append(num)
            
            second_highest = find_second_highest(numbers)
            print("Second highest element:", second_highest)
    except ValueError:
        print("Invalid input. Please enter integers only.")