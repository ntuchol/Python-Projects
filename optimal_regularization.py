from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

        ridge_reg = Ridge()

        params = {'alpha': [0.01, 0.1, 1.0, 10.0, 100.0]}

        grid_search = GridSearchCV(ridge_reg, params, cv=5, scoring='neg_mean_squared_error')
        grid_search.fit(X_train, y_train)

        best_alpha = grid_search.best_params_['alpha']
        print(f"Optimal alpha: {best_alpha}")
