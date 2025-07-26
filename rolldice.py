import random

def roll_dice(num_dice, num_sides):
    results = [random.randint(1, num_sides) for _ in range(num_dice)]
    return results

num_dice = 2  
num_sides = 6  
rolls = roll_dice(num_dice, num_sides)

print(f"You rolled: {rolls}")
print(f"Total: {sum(rolls)}")
