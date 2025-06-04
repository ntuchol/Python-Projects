def count_odd_numbers_loop(numbers):
    count = 0
    for number in numbers:
        if number % 2 != 0:
            count += 1
    return count

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_count = count_odd_numbers_loop(numbers)
print(f"Number of odd numbers: {odd_count}") # Output: Number of odd numbers: 5