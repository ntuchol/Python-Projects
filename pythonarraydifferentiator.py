import numpy as np

def differentiate_array(arr, spacing=1):
  return np.diff(arr) / spacing

# Example usage:
arr = np.array([1, 3, 6, 10, 15])
derivatives = differentiate_array(arr)
print(derivatives)  # Output: [2. 3. 4. 5.]

# Example with uneven spacing
arr2 = np.array([1, 4, 9, 16])
spacing = np.array([1, 2, 1]) # Spacing between points
derivatives2 = np.diff(arr2) / spacing
print(derivatives2) # Output: [3.  2.5 7.]
     