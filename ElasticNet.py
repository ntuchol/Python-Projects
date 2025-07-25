import numpy as np
from sklearn.linear_model import ElasticNetCV
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

X, y = make_regression(n_samples=100, n_features=10, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

elastic_net_cv = ElasticNetCV(
    l1_ratio=[.1, .5, .7, .9, .95, .99, 1],  # Example l1_ratio values to search
    alphas=np.logspace(-4, 0, 10),         # Example alpha values to search (10 values from 10^-4 to 10^0)
    cv=5,                                  # 5-fold cross-validation
    random_state=42,
    n_jobs=-1                              # Use all available CPU cores for parallel processing
)

elastic_net_cv.fit(X_train, y_train)

optimal_alpha = elastic_net_cv.alpha_
optimal_l1_ratio = elastic_net_cv.l1_ratio_

print(f"Optimal alpha: {optimal_alpha}")
print(f"Optimal l1_ratio: {optimal_l1_ratio}")

score = elastic_net_cv.score(X_test, y_test)
print(f"R-squared score on test set with optimal parameters: {score}")

best_elastic_net_model = elastic_net_cv
