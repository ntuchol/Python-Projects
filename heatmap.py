import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Create a sample 2D dataset
data = np.random.rand(10, 10)

# Create the heatmap
sns.heatmap(data)

# Display the plot
plt.show()
