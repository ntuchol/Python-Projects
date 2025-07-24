import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
     poly = PolynomialFeatures(degree=n) # n is the desired polynomial degree
    X_poly = poly.fit_transform(X)
    model = LinearRegression()
    model.fit(X_poly, y)
     X_new_poly = poly.transform(X_new) # Transform new data for prediction
    predictions = model.predict(X_new_poly)