import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_pacf
import pandas as pd # Assuming you have a pandas DataFrame with your time series data

# Assuming you have your data loaded into these pandas Series:
# milk_volume: Original milk volume time series
# milk_volume_diff: Differenced milk volume time series
# tree_rings: Tree ring time series

# Example data (replace with your actual data loading)
# For milk volume (assuming some data like in the Kaggle example)
milk_volume = pd.Series([12, 10, 15, 13, 16, 14, 18, 17, 20, 19, 22, 21]) 
milk_volume_diff = milk_volume.diff().dropna()  # Calculate the difference and remove the first NaN
tree_rings = pd.Series([100, 102, 101, 105, 103, 106, 104, 108, 107, 109, 108, 110])

# Plotting the PACF for Milk Volume
plt.figure(figsize=(10, 5))
plot_pacf(milk_volume, lags=20) # Adjust lags as needed based on your data frequency
plt.title("PACF Plot - Milk Volume")
plt.xlabel("Lag")
plt.ylabel("Partial Autocorrelation")
plt.grid(True)
plt.show()

# Plotting the PACF for Differenced Milk Volume
plt.figure(figsize=(10, 5))
plot_pacf(milk_volume_diff, lags=20) # Adjust lags as needed
plt.title("PACF Plot - Differenced Milk Volume")
plt.xlabel("Lag")
plt.ylabel("Partial Autocorrelation")
plt.grid(True)
plt.show()

# Plotting the PACF for Tree Rings
plt.figure(figsize=(10, 5))
plot_pacf(tree_rings, lags=20) # Adjust lags as needed, considering expected correlation length
plt.title("PACF Plot - Tree Rings")
plt.xlabel("Lag")
plt.ylabel("Partial Autocorrelation")
plt.grid(True)
plt.show()