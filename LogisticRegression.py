import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# 1. Load Data (example with a dummy dataset)
# data = pd.read_csv('your_dataset.csv')
# X = data.drop('target_variable', axis=1) # Independent variables
# y = data['target_variable'] # Dependent variable

# For demonstration, create a sample dataset
from sklearn.datasets import make_classification
X, y = make_classification(n_samples=1000, n_features=10, n_classes=2, random_state=42)

# 2. Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Initialize and train the model
model = LogisticRegression(solver='liblinear', random_state=42) # 'liblinear' is a good default solver for small datasets
model.fit(X_train, y_train)

# 4. Make predictions
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test) # Probabilities for each class

# 5. Evaluate performance
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))