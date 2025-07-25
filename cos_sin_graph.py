import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100) 

y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure(figsize=(8, 6)) # Set the figure size for better visualization
plt.plot(x, y_sin, label='sin(x)', color='blue') # Plot sine function
plt.plot(x, y_cos, label='cos(x)', color='red')  # Plot cosine function

plt.xlabel('Angle (radians)')
plt.ylabel('Amplitude')
plt.title('Sine and Cosine Functions')

plt.legend()

plt.grid(True)

plt.show()
