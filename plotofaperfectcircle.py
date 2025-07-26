import matplotlib.pyplot as plt
import numpy as np

radius = 1
theta = np.linspace(0, 2 * np.pi, 100)  
x = radius * np.cos(theta)  
y = radius * np.sin(theta) 

plt.figure(figsize=(6, 6)) 
plt.plot(x, y, label="Circle")
plt.gca().set_aspect('equal', adjustable='box')  
plt.title("Perfect Circle")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()
