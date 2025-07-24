import statsmodels.api as sm
import pandas as pd
    y = df['dependent_var']
    X = df[['independent_var1', 'independent_var2']]
    X = sm.add_constant(X)
    model = sm.OLS(y, X)
    results = model.fit()
    print(results.summary())