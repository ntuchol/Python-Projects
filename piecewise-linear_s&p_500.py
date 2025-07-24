import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import pwlf

# Download S&P 500 historical data
data = yf.download('^GSPC', start='2010-01-01', end='2025-01-01', auto_adjust=True)
sp500_prices = data['Close'].values
dates = np.arange(len(sp500_prices))

# Initialize pwlf with your data
my_pwlf = pwlf.PiecewiseLinFit(dates, sp500_prices)

# Fit for a specified number of line segments (e.g., 3)
breaks = my_pwlf.fit(3)
print("Breakpoint locations:", breaks)

# Predict values for plotting the fitted line
x_hat = np.linspace(dates.min(), dates.max(), 100)
y_hat = my_pwlf.predict(x_hat)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(dates, sp500_prices, 'o', label='S&P 500 Data')
plt.plot(x_hat, y_hat, '-', color='red', label='Piecewise Linear Fit')
plt.xlabel("Days since 2010-01-01")
plt.ylabel("S&P 500 Price")
plt.title("S&P 500 Piecewise Linear Fit")
plt.legend()
plt.grid(True)
plt.show()