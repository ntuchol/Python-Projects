import numpy as np

def rms(data):
  """
  Calculates the root mean square of a list or array of numbers.

  Args:
    data: A list or array of numbers.

  Returns:
    The root mean square of the data.
  """
  squares = [x**2 for x in data]
  mean_of_squares = sum(squares) / len(data)
  return np.sqrt(mean_of_squares)

# Example usage
data = [1, 2, 3, 4, 5]
rms_value = rms(data)
print(f"The RMS of {data} is: {rms_value}")

# Using numpy
data = np.array([1, 2, 3, 4, 5])
rms_value_np = np.sqrt(np.mean(data**2))
print(f"The RMS (using numpy) of {data} is: {rms_value_np}")