import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.ar_model import AutoReg

np.random.seed(42)
n = 200
phi1, phi2 = 0.6, -0.3 
noise = np.random.normal(0, 1, n)
data = [0, 0]  

for t in range(2, n):
    data.append(phi1 * data[t-1] + phi2 * data[t-2] + noise[t])

model = AutoReg(data, lags=2)
result = model.fit()

print(result.summary())