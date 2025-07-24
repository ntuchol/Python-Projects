import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

X, y = np.random.rand(100, 5), np.random.rand(100) 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

alphas = [0.1, 0.5, 1.0, 5.0, 10.0, 20.0, 50.0, 100.0, 500.0, 1000.0]

trained_models = []
mse_scores = []
for alpha in alphas:
    ridge_model = Ridge(alpha=alpha)  
    ridge_model.fit(X_train, y_train)  
    y_pred = ridge_model.predict(X_test) 
    mse = mean_squared_error(y_test, y_pred) 

    trained_models.append(ridge_model)
    mse_scores.append(mse)

    print(f"Alpha: {alpha}, MSE: {mse:.4f}")


best_alpha_index = np.argmin(mse_scores)
best_alpha = alphas[best_alpha_index]
best_mse = mse_scores[best_alpha_index]

print(f"\nBest Alpha: {best_alpha}, Lowest MSE: {best_mse:.4f}")
