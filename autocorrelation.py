import pandas as pd

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

series = pd.Series(data)

lag = 1
autocorr = series.autocorr(lag)
print(f"Autocorrelation at lag {lag}: {autocorr}")
