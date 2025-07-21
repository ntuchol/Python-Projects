import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create sample data
data = np.random.rand(5, 5) # A 5x5 array of random values
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E'], index=['Row1', 'Row2', 'Row3', 'Row4', 'Row5'])

# Create the heatmap
plt.figure(figsize=(8, 6)) # Set the figure size for better readability
sns.heatmap(df, annot=True, cmap='viridis', fmt=".2f", linewidths=.5)

# Add a title
plt.title('Sample Seaborn Heatmap')

# Display the plot
plt.show()
