import random
from functools import reduce

def average_of_random_list(lists):
    # Randomly select a list
    chosen_list = random.choice(lists)
    
    # Use reduce to calculate the sum of the chosen list
    total = reduce(lambda x, y: x + y, chosen_list)
    
    # Calculate the average
    average = total / len(chosen_list) if chosen_list else 0
    
    return average

# Example usage
lists = [[10, 20, 30], [5, 15, 25, 35], [1, 2, 3, 4, 5]]
print(average_of_random_list(lists))