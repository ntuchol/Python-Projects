    import statsmodels.api as sm
    import numpy as np

    # Sample data
    X = np.random.rand(100, 2)  # Independent variables
    y = 2 * X[:, 0] + 3 * X[:, 1] + np.random.randn(100) * 0.5 # Dependent variable

    # Add a constant for the intercept
    X = sm.add_constant(X)

    # Fit the OLS model
    model = sm.OLS(y, X).fit()

    # Access the AIC value
    aic_value = model.aic
    print(f"AIC: {aic_value}")
