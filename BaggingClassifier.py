from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_iris 
iris = load_iris()
X, y = iris.data, iris.target
knn = KNeighborsClassifier(n_neighbors=5) 
knn_scores = cross_val_score(knn, X, y, cv=5) 
print("KNN Cross-Validation Scores:", knn_scores)
print("KNN Mean Accuracy:", knn_scores.mean())
bagging_knn = BaggingClassifier(estimator=KNeighborsClassifier(n_neighbors=5), n_estimators=10, random_state=42) 
bagging_knn_scores = cross_val_score(bagging_knn, X, y, cv=5) 
print("BaggingClassifier (KNN base) Cross-Validation Scores:", bagging_knn_scores)
print("BaggingClassifier (KNN base) Mean Accuracy:", bagging_knn_scores.mean())
