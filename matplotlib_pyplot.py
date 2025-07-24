import matplotlib.pyplot as plt
import numpy as np

# Define the interval
x = np.linspace(0, 10, 500)  # 500 points for a smooth curve

# Define the parameter p for f(x)
p_value = 2  # Example value for p

# Define the functions
f_x = np.exp(-x / p_value) * np.sin(np.pi * x)
g_x = np.cos(x)

# Create the plot
plt.figure(figsize=(10, 6))  # Set figure size for better readability
plt.plot(x, f_x, label=f'f(x) = e^(-x/{p_value}) sin(πx)')
plt.plot(x, g_x, label='g(x) = cos(x)')

# Add plot enhancements
plt.title('Plot of f(x) and g(x) over [0, 10]')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()  # Display the legend
plt.grid(True) # Add a grid for better visualization

# Show the plot
plt.show()