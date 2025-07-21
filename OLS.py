import statsmodels.api as sm
import pandas as pd
import numpy as np


    # Example data
    X = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 5, 4, 5])

    # Add a constant for the intercept
    X = sm.add_constant(X)

    # Create the OLS model object
    model = sm.OLS(y, X)

    # Fit the model
    results = model.fit()
    print(results.summary())