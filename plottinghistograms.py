import matplotlib.pyplot as plt
import numpy as np

# Example: Generate some random data
data = np.random.randn(1000) # 1000 random numbers from a standard normal distribution
plt.hist(data, bins=30) # Plot with 30 bins

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Distribution of Data')

plt.show()

