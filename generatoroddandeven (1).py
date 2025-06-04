def even_odd_generator():
    """
    A generator that yields alternating even and odd numbers.
    """
    current_number = 0
    while True:
        if current_number % 2 == 0:  # Even number
            yield current_number
            current_number += 1
        else:  # Odd number
            yield current_number
            current_number += 1