from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 1. Generate or Load Data
X, y = make_classification(n_samples=1000, n_features=20, n_informative=10, n_redundant=10, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 2. Initialize AdaBoost Classifier
# Using a Decision Tree Stump as base estimator
base_classifier = DecisionTreeClassifier(max_depth=1) 
adaboost_model = AdaBoostClassifier(base_estimator=base_classifier, n_estimators=100, learning_rate=1.0, random_state=42)

# 3. Train the Model
adaboost_model.fit(X_train, y_train)

# 4. Make Predictions and Evaluate
y_pred = adaboost_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"AdaBoost Classifier Accuracy: {accuracy}")