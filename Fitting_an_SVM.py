from sklearn.svm import SVC
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=100, n_features=2, n_informative=2,
                               n_redundant=0, n_clusters_per_class=1, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    svm_model = SVC(kernel='rbf', gamma=0.1, C=10.0)

  
    svm_model.fit(X_train, y_train)
    accuracy = svm_model.score(X_test, y_test)
    print(f"Model accuracy on test set: {accuracy:.2f}")