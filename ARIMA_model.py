import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

data = [112, 118, 132, 129, 121, 135, 148, 148, 136, 119, 104, 118]
df = pd.DataFrame(data, columns=["Value"])

model = ARIMA(df["Value"], order=(1, 1, 1))  
fitted_model = model.fit()

print(fitted_model.summary())

forecast = fitted_model.forecast(steps=5)  
print("Forecasted values:", forecast)

plt.plot(df["Value"], label="Original Data")
plt.plot(range(len(df), len(df) + len(forecast)), forecast, label="Forecast", color="red")
plt.legend()
plt.show()