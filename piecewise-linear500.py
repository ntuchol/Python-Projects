import numpy as np
import matplotlib.pyplot as plt
from pwlf import PiecewiseLinFit

# Generate sample data
x = np.linspace(0, 10, 500)
y = np.sin(x) + np.random.randn(500) * 0.2

# Initialize piecewise linear fit with 3 segments
my_pwlf = PiecewiseLinFit(x, y)

# Fit the data
res = my_pwlf.fitfast(3)

# Get the x values of the line segments
x_c = my_pwlf.fit_breaks

# Predict y values
y_hat = my_pwlf.predict(x)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'o', label='Data')
plt.plot(x, y_hat, '-', label='Piecewise Linear Fit')
plt.vlines(x_c[1:-1], y.min(), y.max(), linestyle="--", color="grey", alpha=0.5, label='Break Points')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Piecewise Linear Fit')
plt.show()

# Print the slopes and intercepts of each segment
slopes = my_pwlf.slopes
intercepts = my_pwlf.intercepts
for i in range(len(slopes)):
    print(f"Segment {i+1}: Slope = {slopes[i]:.2f}, Intercept = {intercepts[i]:.2f}")