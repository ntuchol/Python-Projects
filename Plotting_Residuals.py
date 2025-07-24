res = y_true - y_pred
import matplotlib.pyplot as plt
import numpy as np

# Example data (replace with your actual data)
np.random.seed(42)
x = np.random.rand(100) * 10
y_true = 2 * x + 5 + np.random.randn(100) * 2
y_pred = 2 * x + 5  # Simple linear prediction for demonstration

res = y_true - y_pred

plt.figure(figsize=(8, 6))
plt.scatter(y_pred, res)
plt.axhline(y=0, color='r', linestyle='--') # Add a horizontal line at 0 for reference
plt.xlabel("Predicted Values")
plt.ylabel("Residuals")
plt.title("Residual Plot")
plt.grid(True)
plt.show()