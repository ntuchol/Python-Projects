def perfect_squares(limit):
    return [i**2 for i in range(1, limit + 1)]

limit = 10  
squares = perfect_squares(limit)
print(squares)
