import numpy as np

# Create a 5x5x5 cube filled with zeros
cube = np.zeros((5, 5, 5))

# Example: Fill the cube with sequential numbers
for x in range(5):
    for y in range(5):
        for z in range(5):
            cube[x, y, z] = x * 25 + y * 5 + z

print("5x5x5 Cube:")
print(cube)