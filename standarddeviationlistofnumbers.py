import statistics

numbers = [10, 20, 30, 40, 50]
std_dev = statistics.stdev(numbers)
print(f"Standard Deviation: {std_dev}")


import numpy as np

numbers = [10, 20, 30, 40, 50]
std_dev = np.std(numbers, ddof=1)  
print(f"Standard Deviation: {std_dev}")

numbers = [10, 20, 30, 40, 50]


mean = sum(numbers) / len(numbers)

squared_diffs = [(x - mean) ** 2 for x in numbers]

variance = sum(squared_diffs) / (len(numbers) - 1)

std_dev = variance ** 0.5

print(f"Standard Deviation: {std_dev}")
