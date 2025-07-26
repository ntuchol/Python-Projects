import numpy as np

def differentiate_array(arr, spacing=1):
  return np.diff(arr) / spacing

arr = np.array([1, 3, 6, 10, 15])
derivatives = differentiate_array(arr)
print(derivatives)  

arr2 = np.array([1, 4, 9, 16])
spacing = np.array([1, 2, 1]) 
derivatives2 = np.diff(arr2) / spacing
print(derivatives2) 
     
