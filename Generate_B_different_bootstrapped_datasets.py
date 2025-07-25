import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.utils import resample

def train_bootstrapped_trees(X, y, num_trees=10):
    
    trained_trees = []
    n_samples = X.shape[0]

    for i in range(num_trees):
         X_bootstrap, y_bootstrap = resample(X, y, n_samples=n_samples, random_state=i)

        tree = DecisionTreeClassifier(random_state=i) # Using random_state for reproducibility
        tree.fit(X_bootstrap, y_bootstrap)
        trained_trees.append(tree)

    return trained_trees

if __name__ == "__main__":
    from sklearn.datasets import make_classification
    X_data, y_data = make_classification(n_samples=100, n_features=4, n_informative=2,
                                         n_redundant=0, random_state=42)

    num_bootstrapped_trees = 5
    my_trained_trees = train_bootstrapped_trees(X_data, y_data, num_bootstrapped_trees)

    print(f"Successfully trained {len(my_trained_trees)} decision trees.")
