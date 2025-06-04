import numpy as np

# Generate a 1000x1000 array of random floating-point numbers between 0 and 1
random_array = np.random.rand(1000, 1000)

# If you want numbers in a specific range, e.g., between a and b:
# a, b = 10, 20
# random_array = a + (b - a) * np.random.rand(1000, 1000)

print(random_array)