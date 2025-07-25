import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = np.random.rand(5, 5) 
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E'], index=['Row1', 'Row2', 'Row3', 'Row4', 'Row5'])

plt.figure(figsize=(8, 6)) 
sns.heatmap(df, annot=True, cmap='viridis', fmt=".2f", linewidths=.5)

plt.title('Sample Seaborn Heatmap')

plt.show()
