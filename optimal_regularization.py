from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

        # Create a Ridge regression instance
        ridge_reg = Ridge()

        # Define the range of alpha values to search
        params = {'alpha': [0.01, 0.1, 1.0, 10.0, 100.0]}

        # Perform Grid Search with cross-validation
        grid_search = GridSearchCV(ridge_reg, params, cv=5, scoring='neg_mean_squared_error')
        grid_search.fit(X_train, y_train)

        # Get the best alpha value
        best_alpha = grid_search.best_params_['alpha']
        print(f"Optimal alpha: {best_alpha}")