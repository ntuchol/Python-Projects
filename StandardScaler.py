from sklearn.preprocessing import StandardScaler
import numpy as np

# Sample data
X = np.array([[10, 1],
              [20, 2],
              [30, 3],
              [40, 4]])

# Create a StandardScaler object
scaler = StandardScaler()

# Fit the scaler to the data and transform it
scaled_data = scaler.fit_transform(X)

print("Original Data:\n", X)
print("\nScaled Data:\n", scaled_data)