import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.1, 10, 500)  

y = np.log2(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$y = \log_2(x)$', color='blue')

plt.title("Plot of $y = \log_2(x)$", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  
plt.grid(alpha=0.3)
plt.legend(fontsize=12)

plt.show()
