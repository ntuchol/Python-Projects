import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('lynx.csv', index_col='year')

plt.figure(figsize=(10, 6))
plt.plot(data['trappings'])
plt.title('Canadian Lynx Trappings (1821-1934)')
plt.xlabel('Year')
plt.ylabel('Number of Lynx Trapped')
plt.grid(True)
plt.show()
