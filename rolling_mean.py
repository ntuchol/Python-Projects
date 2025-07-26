import pandas as pd

data = {'values': [10, 20, 30, 40, 50, 60, 70]}
df = pd.DataFrame(data)

df['rolling_mean'] = df['values'].rolling(window=3).mean()

print(df)
