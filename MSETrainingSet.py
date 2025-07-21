from sklearn.linear_model import LinearRegression
    # Assuming X_train and y_train are already defined
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred_train = model.predict(X_train)
   from sklearn.metrics import mean_squared_error
    mse_train = mean_squared_error(y_train, y_pred_train)
    print(f"Training MSE: {mse_train}")