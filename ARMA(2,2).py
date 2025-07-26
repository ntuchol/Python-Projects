import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

np.random.seed(42)
n = 200
ar_params = [0.75, -0.25]  
ma_params = [0.65, 0.35]   
noise = np.random.normal(0, 1, n)
data = pd.Series(np.zeros(n))

for t in range(2, n):
    data[t] = (
        ar_params[0] * data[t-1] +
        ar_params[1] * data[t-2] +
        noise[t] +
        ma_params[0] * noise[t-1] +
        ma_params[1] * noise[t-2]
    )

model = ARIMA(data, order=(2, 0, 2))  
fitted_model = model.fit()

print(fitted_model.summary())

plt.figure(figsize=(10, 6))
plt.plot(data, label="Original Data")
plt.plot(fitted_model.fittedvalues, label="Fitted Values", color="red")
plt.legend()
plt.title("ARMA(2,2) Model Fit")
plt.show()