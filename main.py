import numpy as np
from sklearn.decomposition import PCA

def horns_parallel_analysis(data, num_simulations=100, percentile=95):
    n_samples, n_features = data.shape
    original_pca = PCA()
    original_pca.fit(data)
    original_eigenvalues = original_pca.explained_variance_

    random_eigenvalues_collection = []
    for _ in range(num_simulations):
        # Generate random data with same dimensions and distribution as original
        random_data = np.random.normal(size=(n_samples, n_features))
        random_pca = PCA()
        random_pca.fit(random_data)
        random_eigenvalues_collection.append(random_pca.explained_variance_)

    random_eigenvalues_array = np.array(random_eigenvalues_collection)
    percentile_eigenvalues = np.percentile(random_eigenvalues_array, percentile, axis=0)

    # Determine number of components
    num_components = np.sum(original_eigenvalues > percentile_eigenvalues)
    return num_components

# Example usage:
# data = np.random.rand(100, 20) # Replace with your actual data
# optimal_components = horns_parallel_analysis(data)
# print(f"Optimal number of components: {optimal_components}")