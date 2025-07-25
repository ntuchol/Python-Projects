import statsmodels.api as sm
import numpy as np

X = np.random.rand(100, 2)  
y = 2 * X[:, 0] + 3 * X[:, 1] + np.random.randn(100) * 0.5 
X = sm.add_constant(X)

model = sm.OLS(y, X).fit()

aic_value = model.aic
print(f"AIC: {aic_value}")
