import pandas as pd
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(X_train) 
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test) 
data = {'feature1': [10, 20, 30, 40, 50],
        'feature2': [100, 200, 150, 250, 120]}
df = pd.DataFrame(data)

scaler = MinMaxScaler()

scaled_data = scaler.fit_transform(df)

df_scaled = pd.DataFrame(scaled_data, columns=df.columns)

print(df_scaled)
