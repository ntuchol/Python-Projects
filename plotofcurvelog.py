import numpy as np
import matplotlib.pyplot as plt

# Define the x values (avoiding x <= 0 since log is undefined there)
x = np.linspace(0.1, 10, 500)  # Start from 0.1 to avoid log(0)

# Define the function y = log2(x)
y = np.log2(x)

# Plot the curve
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$y = \log_2(x)$', color='blue')

# Add labels, title, and grid
plt.title("Plot of $y = \log_2(x)$", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # x-axis
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  # y-axis
plt.grid(alpha=0.3)
plt.legend(fontsize=12)

# Show the plot
plt.show()