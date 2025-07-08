import random
def random_walk_1d(steps):
    position = 0
    walk = [position]
    
    for _ in range(steps):
        step = random.choice([-1, 1])  # Move left (-1) or right (+1)
        position += step
        walk.append(position)
    
    return walk

# Simulate a random walk with 100 steps
walk = random_walk_1d(100)
print(walk)