import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 1. Load your dataset (replace 'your_dataset.csv' with your actual file)
# For demonstration, let's create a dummy dataset
from sklearn.datasets import make_classification
X, y = make_classification(n_samples=1000, n_features=20, n_informative=10, n_redundant=5, random_state=42)
df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(X.shape[1])])
df['target'] = y

# 2. Separate features (X) and target (y)
X = df.drop('target', axis=1)
y = df['target']

# 3. Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. Initialize the Random Forest Classifier
# n_estimators: Number of trees in the forest.
# random_state: Controls the randomness of the bootstrapping and feature selection for reproducibility.
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# 5. Train the model
rf_model.fit(X_train, y_train)

# 6. Make predictions on the test set
y_pred = rf_model.predict(X_test)

# 7. Evaluate the model's performance
print("Model Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Optional: Feature Importance
# print("\nFeature Importances:")
# for feature, importance in zip(X.columns, rf_model.feature_importances_):
#     print(f"{feature}: {importance:.4f}")