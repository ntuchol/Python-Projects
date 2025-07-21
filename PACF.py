import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.graphics.tsaplots import plot_pacf

# Assuming your time series data is stored in pandas Series objects
# Example: Create some sample data for demonstration
# Replace these with your actual data loading methods

# Milk volume time series
milk_volume = pd.Series([
    266.0, 272.9, 275.6, 272.5, 271.8, 274.6, 281.8, 283.3, 286.9, 284.4,
    286.3, 292.0, 290.7, 293.4, 297.1, 298.1, 301.4, 302.3, 304.7, 309.3,
    311.9, 314.9, 318.0, 319.8, 321.4, 324.9, 326.6, 330.1, 334.8, 336.5,
    339.2, 342.3, 345.5, 346.8, 350.4, 353.4, 356.1, 360.7, 362.4, 365.4,
    369.8, 372.4, 374.8, 378.2, 381.8, 384.8, 388.8, 392.4, 396.4, 400.4,
    403.4, 406.4, 409.8, 412.4, 415.8, 418.8, 422.4, 425.8, 428.8, 432.4
])

# Differenced milk volume
differenced_milk_volume = milk_volume.diff().dropna()

# Tree rings series (example - replace with your actual tree rings data)
tree_rings = pd.Series([
    1.2, 1.3, 1.1, 1.4, 1.2, 1.5, 1.3, 1.1, 1.4, 1.2, 1.5, 1.3, 1.1, 1.4,
    1.2, 1.5, 1.3, 1.1, 1.4, 1.2, 1.5, 1.3, 1.1, 1.4, 1.2, 1.5, 1.3, 1.1
])

# Create subplots for better visualization
fig, axes = plt.subplots(3, 1, figsize=(10, 15))

# Plot PACF for Milk Volume
plot_pacf(milk_volume, ax=axes[0], lags=20)
axes[0].set_title("PACF Plot of Milk Volume")
axes[0].set_xlabel("Lag")
axes[0].set_ylabel("Partial Autocorrelation")

# Plot PACF for Differenced Milk Volume
plot_pacf(differenced_milk_volume, ax=axes[1], lags=20)
axes[1].set_title("PACF Plot of Differenced Milk Volume")
axes[1].set_xlabel("Lag")
axes[1].set_ylabel("Partial Autocorrelation")

# Plot PACF for Tree Rings
plot_pacf(tree_rings, ax=axes[2], lags=10)  # Adjust lags based on your data length
axes[2].set_title("PACF Plot of Tree Rings")
axes[2].set_xlabel("Lag")
axes[2].set_ylabel("Partial Autocorrelation")

plt.tight_layout()  # Adjust subplot parameters for a tight layout
plt.show()