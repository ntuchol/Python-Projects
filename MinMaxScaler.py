import pandas as pd
from sklearn.preprocessing import MinMaxScaler

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