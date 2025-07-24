from sklearn.linear_model import LassoCV
    lasso_cv_model = LassoCV(cv=5, random_state=42).fit(X_train, y_train)
optimal_alpha = lasso_cv_model.alpha_
    print(f"The optimal alpha for Lasso regression is: {optimal_alpha}")