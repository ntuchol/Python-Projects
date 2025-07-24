import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
import numpy as np

# 1. Load sample data (replace with your own dataset)
iris = load_iris()
X = iris.data
y = iris.target

# 2. Define a range of K values to test
k_values = range(1, 21)  # Testing K from 1 to 20

# 3. Store mean cross-validated accuracies
mean_accuracies = []

# 4. Loop through K values and perform 5-fold cross-validation
for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X, y, cv=5, scoring='accuracy')
    mean_accuracies.append(np.mean(scores))

# 5. Plot the mean cross-validated accuracy
plt.figure(figsize=(10, 6))
plt.plot(k_values, mean_accuracies, marker='o', linestyle='-')
plt.title('Mean Cross-Validated Accuracy vs. K for KNN (5-Fold CV)')
plt.xlabel('Number of Neighbors (K)')
plt.ylabel('Mean Cross-Validated Accuracy')
plt.xticks(k_values)
plt.grid(True)
plt.show()