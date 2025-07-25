import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_pacf
import pandas as pd # Assuming you have a pandas DataFrame with your time series data


milk_volume = pd.Series([12, 10, 15, 13, 16, 14, 18, 17, 20, 19, 22, 21]) 
milk_volume_diff = milk_volume.diff().dropna()  
tree_rings = pd.Series([100, 102, 101, 105, 103, 106, 104, 108, 107, 109, 108, 110])

plt.figure(figsize=(10, 5))
plot_pacf(milk_volume, lags=20)
plt.title("PACF Plot - Milk Volume")
plt.xlabel("Lag")
plt.ylabel("Partial Autocorrelation")
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
plot_pacf(milk_volume_diff, lags=20) # Adjust lags as needed
plt.title("PACF Plot - Differenced Milk Volume")
plt.xlabel("Lag")
plt.ylabel("Partial Autocorrelation")
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
plot_pacf(tree_rings, lags=20) 
plt.title("PACF Plot - Tree Rings")
plt.xlabel("Lag")
plt.ylabel("Partial Autocorrelation")
plt.grid(True)
plt.show()
