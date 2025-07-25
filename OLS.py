import statsmodels.api as sm
import pandas as pd
import numpy as np


    X = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 5, 4, 5])

    X = sm.add_constant(X)

    model = sm.OLS(y, X)

    results = model.fit()
    print(results.summary())
