import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

np.random.seed(0)
X = 2 * np.random.rand(100, 1) 
y = 4 + 3 * X + np.random.randn(100, 1) 

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

residuals = y - y_pred

plt.figure(figsize=(8, 6))
plt.scatter(y, residuals, alpha=0.6)  
plt.axhline(y=0, color='r', linestyle='--', linewidth=2)  
plt.title('Residual Plot (Residuals vs. True Values)')
plt.xlabel('True Values (y)')
plt.ylabel('Residuals')
plt.grid(True)
plt.show()
