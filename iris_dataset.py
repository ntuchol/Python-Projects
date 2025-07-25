from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris # Example dataset
from sklearn.metrics import accuracy_score

iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

training_errors = []
test_errors = []
k_values = range(1, 21) # Test K from 1 to 20

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)

    y_train_pred = knn.predict(X_train)
    train_error = 1 - accuracy_score(y_train, y_train_pred)
    training_errors.append(train_error)

    y_test_pred = knn.predict(X_test)
    test_error = 1 - accuracy_score(y_test, y_test_pred)
    test_errors.append(test_error)

plt.figure(figsize=(10, 6))
plt.plot(k_values, training_errors, label='Training Error')
plt.plot(k_values, test_errors, label='Test Error')
plt.xlabel('Number of Neighbors (K)')
plt.ylabel('Error Rate')
plt.title('Training and Test Error vs. K for KNN')
plt.xticks(k_values)
plt.legend()
plt.grid(True)
plt.show()
iris_df = load_iris(as_frame=True)

iris = load_iris()
X = iris.data  
y = iris.target 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=50, random_state=42)

print(f"Shape of X_train: {X_train.shape}")
print(f"Shape of X_test: {X_test.shape}")
print(f"Shape of y_train: {y_train.shape}")
print(f"Shape of y_test: {y_test.shape}")

def classify_iris_by_petal_length(petal_length, threshold):
  if petal_length < threshold:
    return 0
  else:
    return 2
