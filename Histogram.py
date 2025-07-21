import matplotlib.pyplot as plt
import numpy as np

# Generate some sample data (e.g., from a normal distribution)
data = np.random.randn(1000)

# Create a histogram
plt.hist(data, bins=30, edgecolor='black') # bins control the number of intervals
plt.title('Histogram of Sample Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()