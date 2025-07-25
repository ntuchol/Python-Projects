from sklearn.preprocessing import StandardScaler
import numpy as np

X = np.array([[10, 1],
              [20, 2],
              [30, 3],
              [40, 4]])

scaler = StandardScaler()

scaled_data = scaler.fit_transform(X)

print("Original Data:\n", X)
print("\nScaled Data:\n", scaled_data)
