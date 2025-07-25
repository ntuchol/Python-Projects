from sklearn.cluster import KMeans
import numpy as np

X = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])

kmeans = KMeans(n_clusters=2, random_state=0, n_init='auto')

kmeans.fit(X)

labels = kmeans.labels_

centroids = kmeans.cluster_centers_

print("Cluster Labels:", labels)
print("Cluster Centroids:", centroids)
