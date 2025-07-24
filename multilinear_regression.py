from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit(X, y)
    predictions = model.predict(new_X)
    coefficients = model.coef_
    intercept = model.intercept_