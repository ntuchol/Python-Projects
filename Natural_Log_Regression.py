import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 5, 10, 17, 26])

y_log = np.log(y)
model = LinearRegression()
model.fit(X, y_log)
y_log_pred = model.predict(X)
y_pred_original_scale = np.exp(y_log_pred)