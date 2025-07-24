import pandas as pd
import numpy as np
import statsmodels.api as sm

# 1. Prepare sample data
data = {'X': [1, 2, 3, 4, 5],
        'Y': [2, 4, 5, 4, 6]}
df = pd.DataFrame(data)

# Define dependent and independent variables
Y = df['Y']
X = df['X']

# 2. Add a constant term for the intercept
X = sm.add_constant(X)

# 3. Perform OLS regression
model = sm.OLS(Y, X)
results = model.fit()

# 4. Print the summary of the results
print(results.summary())