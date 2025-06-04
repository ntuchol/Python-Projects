import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Date': pd.date_range(start='2023-01-01', periods=20),
    'Value': [10, 12, 15, 14, 13, 16, 18, 20, 19, 17, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]
}
df = pd.DataFrame(data)

# Calculate the moving average (e.g., 5-period moving average)
df['Moving_Avg'] = df['Value'].rolling(window=5).mean()

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Value'], label='Original Data', marker='o')
plt.plot(df['Date'], df['Moving_Avg'], label='5-Period Moving Average', color='orange', linewidth=2)
plt.title('Moving Average Line')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.grid()
plt.show()