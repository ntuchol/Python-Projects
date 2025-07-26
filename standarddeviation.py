import statistics
import numpy

data = [4, 8, 6, 5, 3, 2, 8, 9, 2, 5]

std_dev_statistics = statistics.stdev(data)
print(f"Standard deviation using statistics: {std_dev_statistics}")

std_dev_numpy = numpy.std(data)
print(f"Standard deviation using numpy: {std_dev_numpy}")

n = len(data)
mean = sum(data) / n
deviations = [(x - mean) ** 2 for x in data]
variance = sum(deviations) / (n - 1)
std_dev_manual = variance ** 0.5
print(f"Standard deviation calculated manually: {std_dev_manual}")
