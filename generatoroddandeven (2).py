def even_odd_generator():
    current_number = 0
    while True:
        if current_number % 2 == 0:  # Even number
            yield current_number
            current_number += 1
        else:  
            yield current_number
            current_number += 1
