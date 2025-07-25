import random
from functools import reduce

def average_of_random_list(lists):
    chosen_list = random.choice(lists)
    
    total = reduce(lambda x, y: x + y, chosen_list)
    
    average = total / len(chosen_list) if chosen_list else 0
    
    return average

lists = [[10, 20, 30], [5, 15, 25, 35], [1, 2, 3, 4, 5]]
print(average_of_random_list(lists))
