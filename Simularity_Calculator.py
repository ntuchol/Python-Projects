import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Example with 1D arrays
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])
similarity = cosine_similarity(vector1.reshape(1, -1), vector2.reshape(1, -1))[0][0]
print(f"Cosine Similarity (1D arrays): {similarity}")

# Example with 2D arrays (e.g., from TF-IDF)
matrix = np.array([[1, 0, 1, 0], [0, 1, 1, 0], [1, 1, 0, 1]])
# Calculate similarity between all pairs of rows in the matrix
similarity_matrix = cosine_similarity(matrix)
print(f"Cosine Similarity Matrix:\n{similarity_matrix}")

def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    if union == 0:
        return 0.0  # Or handle as desired for empty sets
    return intersection / union

list1 = ["apple", "banana", "orange"]
list2 = ["banana", "grape", "orange"]
set1 = set(list1)
set2 = set(list2)
similarity = jaccard_similarity(set1, set2)
print(f"Jaccard Similarity: {similarity}")

from Levenshtein import distance

string1 = "kitten"
string2 = "sitting"
dist = distance(string1, string2)
print(f"Levenshtein Distance: {dist}")