    from sklearn.linear_model import RidgeCV
    import numpy as np
    
    X = np.random.rand(100, 5)
    y = 2 * X[:, 0] + 0.5 * X[:, 1] + np.random.randn(100) * 0.1
    alphas = [0.001, 0.01, 0.1, 1.0, 10.0, 100.0]
    # Create a RidgeCV model
    ridge_cv_model = RidgeCV(alphas=alphas, scoring='neg_mean_squared_error', cv=5) # cv=5 for 5-fold cross-validation
    
    # Fit the model to your data
    ridge_cv_model.fit(X, y)
    best_alpha = ridge_cv_model.alpha_
    print(f"The optimal alpha value is: {best_alpha}")