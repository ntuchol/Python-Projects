from sklearn.linear_model import ElasticNetCV
from sklearn.datasets import make_regression # For sample data
    import numpy as np
        X, y = make_regression(n_samples=100, n_features=10, random_state=0)
       alphas = np.logspace(-4, 4, 50) # Example: 50 values from 10^-4 to 10^4
       l1_ratios = [.1, .5, .7, .9, .95, .99, 1] # Example: various mixes
model = ElasticNetCV(l1_ratio=l1_ratios, alphas=alphas, cv=5, random_state=0)
model.fit(X, y)