import numpy as np
import pandas as pd

# Using NumPy array
target_vector_np = np.array([10, 20, 30, 40, 50])
print("NumPy Target Vector:\n", target_vector_np)

# Using Pandas Series (often derived from a DataFrame column)
data = {'feature1': [1, 2, 3, 4, 5], 'target': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)
target_vector_pd = df['target']
print("\nPandas Target Vector:\n", target_vector_pd)

# Using NumPy array
predictor_matrix_np = np.array([[1, 2],
                                [3, 4],
                                [5, 6],
                                [7, 8],
                                [9, 10]])
print("NumPy Predictor Matrix:\n", predictor_matrix_np)

# Using Pandas DataFrame (common for handling various data types)
data = {'feature1': [1, 2, 3, 4, 5],
        'feature2': [11, 12, 13, 14, 15],
        'feature3': [21, 22, 23, 24, 25]}
predictor_matrix_pd = pd.DataFrame(data)
print("\nPandas Predictor Matrix:\n", predictor_matrix_pd)