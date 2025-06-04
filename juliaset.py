import numpy as np
import matplotlib.pyplot as plt

def julia_set(width, height, zoom, c, max_iter):
    # Create a grid of complex numbers
    x = np.linspace(-1.5, 1.5, width)
    y = np.linspace(-1.5, 1.5, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y

    # Initialize the iteration count array
    iteration_counts = np.zeros(Z.shape, dtype=int)

    # Iterate to determine if points belong to the Julia set
    for i in range(max_iter):
        mask = np.abs(Z) <= 2
        Z[mask] = Z[mask] ** 2 + c
        iteration_counts[mask] += 1

    return iteration_counts

# Parameters for the Julia set
width, height = 800, 800
zoom = 1
c = complex(-0.7, 0.27015)  # Change this to explore different Julia sets
max_iter = 300

# Generate the Julia set
julia = julia_set(width, height, zoom, c, max_iter)

# Plot the Julia set
plt.figure(figsize=(10, 10))
plt.imshow(julia, cmap="inferno", extent=[-1.5, 1.5, -1.5, 1.5])
plt.colorbar(label="Number of Iterations")
plt.title("Julia Set")
plt.xlabel("Re")
plt.ylabel("Im")
plt.show()
