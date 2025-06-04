To calculate the standard deviation of a list of numbers in Python, you can use the statistics module or implement it manually. Here are three approaches:

1. Using the statistics module (simplest method)
Copy the code
import statistics

numbers = [10, 20, 30, 40, 50]
std_dev = statistics.stdev(numbers)
print(f"Standard Deviation: {std_dev}")

2. Using NumPy (useful for larger datasets)
Copy the code
import numpy as np

numbers = [10, 20, 30, 40, 50]
std_dev = np.std(numbers, ddof=1)  # ddof=1 for sample standard deviation
print(f"Standard Deviation: {std_dev}")

3. Manual Calculation (for learning purposes)
Copy the code
numbers = [10, 20, 30, 40, 50]

# Step 1: Calculate the mean
mean = sum(numbers) / len(numbers)

# Step 2: Calculate squared differences from the mean
squared_diffs = [(x - mean) ** 2 for x in numbers]

# Step 3: Compute the variance (sample variance uses n-1)
variance = sum(squared_diffs) / (len(numbers) - 1)

# Step 4: Take the square root of the variance
std_dev = variance ** 0.5

print(f"Standard Deviation: {std_dev}")


Each method is valid, so you can choose based on your needs or familiarity with libraries.