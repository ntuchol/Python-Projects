import pandas as pd
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(X_train) # X_train is your training data
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test) # Apply the *same* scaler to test data

# Sample data
data = {'feature1': [10, 20, 30, 40, 50],
        'feature2': [100, 200, 150, 250, 120]}
df = pd.DataFrame(data)

# Initialize the MinMaxScaler
scaler = MinMaxScaler()

# Fit and transform the data
scaled_data = scaler.fit_transform(df)

# Convert back to a DataFrame for better readability (optional)
df_scaled = pd.DataFrame(scaled_data, columns=df.columns)

print(df_scaled)