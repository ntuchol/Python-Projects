import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.utils import resample

def train_bootstrapped_trees(X, y, num_trees=10):
    """
    Generates B bootstrapped training datasets and trains a new decision tree
    on each dataset.

    Args:
        X (array-like): The features of the original training data.
        y (array-like): The target variable of the original training data.
        num_trees (int): The number of bootstrapped datasets and trees to generate.

    Returns:
        list: A list of trained DecisionTreeClassifier models.
    """
    trained_trees = []
    n_samples = X.shape[0]

    for i in range(num_trees):
        # 1. Generate a bootstrapped training dataset (sampling with replacement)
        # resample returns a tuple of (resampled_X, resampled_y)
        X_bootstrap, y_bootstrap = resample(X, y, n_samples=n_samples, random_state=i)

        # 2. Train a new decision tree on the bootstrapped dataset
        tree = DecisionTreeClassifier(random_state=i) # Using random_state for reproducibility
        tree.fit(X_bootstrap, y_bootstrap)
        trained_trees.append(tree)

    return trained_trees

# Example Usage:
if __name__ == "__main__":
    # Create some dummy data
    from sklearn.datasets import make_classification
    X_data, y_data = make_classification(n_samples=100, n_features=4, n_informative=2,
                                         n_redundant=0, random_state=42)

    # Generate 5 bootstrapped trees
    num_bootstrapped_trees = 5
    my_trained_trees = train_bootstrapped_trees(X_data, y_data, num_bootstrapped_trees)

    print(f"Successfully trained {len(my_trained_trees)} decision trees.")
    # You can now use these trees for predictions, e.g., in a Random Forest ensemble
    # by aggregating their predictions (e.g., majority voting for classification).
Explanation: