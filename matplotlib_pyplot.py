import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 500)  

p_value = 2  

f_x = np.exp(-x / p_value) * np.sin(np.pi * x)
g_x = np.cos(x)

plt.figure(figsize=(10, 6)) 
plt.plot(x, f_x, label=f'f(x) = e^(-x/{p_value}) sin(πx)')
plt.plot(x, g_x, label='g(x) = cos(x)')

plt.title('Plot of f(x) and g(x) over [0, 10]')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()  
plt.grid(True)
plt.show()
