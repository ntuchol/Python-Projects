from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LogisticRegression
import numpy as np

# Sample data (replace with your actual data)
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
y = np.array([0, 1, 0, 1, 0, 1])

# Initialize a model (e.g., Logistic Regression)
model = LogisticRegression()

# Define KFold cross-validation with k=3 splits
kf = KFold(n_splits=3, shuffle=True, random_state=42)

# Perform cross-validation and get scores
scores = cross_val_score(model, X, y, cv=kf, scoring='accuracy')

# Print the scores for each fold and the average score
print("Scores for each fold:", scores)
print("Average score:", np.mean(scores))
