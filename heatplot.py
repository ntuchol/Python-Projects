import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 

data = np.random.rand(10, 8)
df = pd.DataFrame(data, columns=[f'Col_{i}' for i in range(8)])
sns.heatmap(df)
plt.show() 


