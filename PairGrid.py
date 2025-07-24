import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd # Assuming you have data in a pandas DataFrame
# Example: Load a built-in dataset
    data = sns.load_dataset("iris")
    g = sns.PairGrid(data)
    g.map_lower(sns.scatterplot)
    g.map_diag(sns.histplot) # Histograms on the diagonal
    g.map_lower(sns.regplot, lowess=True, scatter_kws={'alpha': 0.5})
    plt.show()