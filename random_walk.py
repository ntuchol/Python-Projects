import random
def random_walk_1d(steps):
    position = 0
    walk = [position]
    
    for _ in range(steps):
        step = random.choice([-1, 1])  
        position += step
        walk.append(position)
    
    return walk

walk = random_walk_1d(100)
print(walk)
