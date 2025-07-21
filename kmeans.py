from sklearn.cluster import KMeans
import numpy as np

X = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])
kmeans = KMeans(n_clusters=2, random_state=0, n_init='auto') # n_init='auto' for scikit-learn >= 1.2
kmeans.fit(X)
