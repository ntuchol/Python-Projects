import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Fetch S&P 500 index data from 2000 onwards
sp500 = yf.Ticker("^GSPC")
sp500_data = sp500.history(start="2000-01-01")

# Extract the 'Close' price and calculate daily returns
sp500_data = sp500_data[["Close"]]
sp500_data["Daily Return %"] = sp500_data["Close"].pct_change() * 100
sp500_data.dropna(inplace=True)

# Plotting the daily returns
plt.figure(figsize=(10, 6))
plt.plot(sp500_data.index, sp500_data["Daily Return %"])
plt.title("S&P 500 Daily Returns (21st Century)")
plt.xlabel("Date")
plt.ylabel("Daily Return (%)")
plt.grid(True)
plt.show()