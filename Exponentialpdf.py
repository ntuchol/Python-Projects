from scipy.stats import expon
import numpy as np
import matplotlib.pyplot as plt

# Define the rate parameter (lambda)
rate_param = 0.5 

# The scale parameter for scipy.stats.expon is the inverse of the rate parameter
scale_param = 1 / rate_param

# Create an expon object with the specified scale
exp_dist = expon(scale=scale_param)

# Generate x values for plotting the PDF
x_values = np.linspace(0, 10, 100)

# Calculate the PDF for each x value
pdf_values = exp_dist.pdf(x_values)

# Plot the PDF
plt.plot(x_values, pdf_values, label=f'Exponential PDF (λ={rate_param})')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.title('Exponential Distribution PDF')
plt.grid(True)
plt.legend()
plt.show()