import numpy as np
import matplotlib.pyplot as plt

# Generate x-values from 0 to 2*pi (a full cycle)
# np.linspace creates evenly spaced numbers over a specified interval.
x = np.linspace(0, 2 * np.pi, 100) 

# Calculate the sine and cosine of the x-values
y_sin = np.sin(x)
y_cos = np.cos(x)

# Create the plot
plt.figure(figsize=(8, 6)) # Set the figure size for better visualization
plt.plot(x, y_sin, label='sin(x)', color='blue') # Plot sine function
plt.plot(x, y_cos, label='cos(x)', color='red')  # Plot cosine function

# Add labels and title
plt.xlabel('Angle (radians)')
plt.ylabel('Amplitude')
plt.title('Sine and Cosine Functions')

# Add a legend to distinguish the lines
plt.legend()

# Add a grid for better readability
plt.grid(True)

# Display the plot
plt.show()