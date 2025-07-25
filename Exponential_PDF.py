from scipy.stats import expon
import numpy as np
import matplotlib.pyplot as plt

rate_param = 0.5 

scale_param = 1 / rate_param

exp_dist = expon(scale=scale_param)

x_values = np.linspace(0, 10, 100)

pdf_values = exp_dist.pdf(x_values)

plt.plot(x_values, pdf_values, label=f'Exponential PDF (λ={rate_param})')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.title('Exponential Distribution PDF')
plt.grid(True)
plt.legend()
plt.show()
