import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA

np.random.seed(42)
n = 100
phi = 0.8  
noise = np.random.normal(0, 1, n)
data = [0]  
for t in range(1, n):
    data.append(phi * data[t-1] + noise[t])

model = ARIMA(data, order=(1, 0, 0))  
result = model.fit()

print(result.summary())