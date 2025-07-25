import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc

X, y = make_classification(n_samples=1000, n_features=20, n_informative=10, n_redundant=5, random_state=42)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model_original = LogisticRegression(solver='liblinear', random_state=42)
model_original.fit(X_train, y_train)

model_ridge = LogisticRegression(penalty='l2', solver='liblinear', C=1.0, random_state=42) # C is inverse of regularization strength
model_ridge.fit(X_train, y_train)

y_pred_proba_original = model_original.predict_proba(X_test)[:, 1]
y_pred_proba_ridge = model_ridge.predict_proba(X_test)[:, 1]

fpr_original, tpr_original, _ = roc_curve(y_test, y_pred_proba_original)
roc_auc_original = auc(fpr_original, tpr_original)

fpr_ridge, tpr_ridge, _ = roc_curve(y_test, y_pred_proba_ridge)
roc_auc_ridge = auc(fpr_ridge, tpr_ridge)

plt.figure(figsize=(8, 6))
plt.plot(fpr_original, tpr_original, color='darkorange', lw=2, label=f'Original LR (AUC = {roc_auc_original:.2f})')
plt.plot(fpr_ridge, tpr_ridge, color='green', lw=2, label=f'Ridge LR (AUC = {roc_auc_ridge:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Random Classifier')

plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc='lower right')
plt.grid(True)
plt.show()
