import matplotlib.pyplot as plt
import numpy as np

# Define the circle parameters
radius = 1
theta = np.linspace(0, 2 * np.pi, 100)  # Angle values from 0 to 2π
x = radius * np.cos(theta)  # X-coordinates
y = radius * np.sin(theta)  # Y-coordinates

# Plot the circle
plt.figure(figsize=(6, 6))  # Ensure the plot is square
plt.plot(x, y, label="Circle")
plt.gca().set_aspect('equal', adjustable='box')  # Equal aspect ratio
plt.title("Perfect Circle")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()