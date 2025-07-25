def find_largest_odd(numbers):
    largest_odd = -1
    for number in numbers:
        if number % 2 != 0 and number > largest_odd:
            largest_odd = number
    return largest_odd
