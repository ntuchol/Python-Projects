import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Generate some sample data for a simple linear regression to illustrate
np.random.seed(0)
X = 2 * np.random.rand(100, 1) # Independent variable
y = 4 + 3 * X + np.random.randn(100, 1) # Dependent variable with some noise

# Fit a linear regression model
model = LinearRegression()
model.fit(X, y)

# Make predictions
y_pred = model.predict(X)

# Calculate residuals
residuals = y - y_pred

# Create the residual plot
plt.figure(figsize=(8, 6))
plt.scatter(y, residuals, alpha=0.6)  # Plot residuals against true 'y' values
plt.axhline(y=0, color='r', linestyle='--', linewidth=2)  # Add a horizontal line at y=0
plt.title('Residual Plot (Residuals vs. True Values)')
plt.xlabel('True Values (y)')
plt.ylabel('Residuals')
plt.grid(True)
plt.show()