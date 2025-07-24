from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

# Sample data
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
y = np.array([3, 5, 7, 9, 11])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Lasso regression model
# alpha is the regularization strength (lambda in some contexts)
# Higher alpha values lead to stronger regularization and more coefficients shrinking to zero
lasso_model = Lasso(alpha=0.1) 

# Fit the model to the training data
lasso_model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = lasso_model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Access the coefficients and intercept
print(f"Coefficients: {lasso_model.coef_}")
print(f"Intercept: {lasso_model.intercept_}")