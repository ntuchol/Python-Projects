import statistics
from scipy.stats import hmean

data = [1, 2, 3, 4, 5]

# Using statistics.harmonic_mean()
harmonic_mean_1 = statistics.harmonic_mean(data)
print(f"Harmonic mean using statistics: {harmonic_mean_1}")

# Using scipy.stats.hmean()
harmonic_mean_2 = hmean(data)
print(f"Harmonic mean using scipy: {harmonic_mean_2}")


#Example with weights using scipy.stats.hmean()
data2 = [1, 4, 7]
weights = [3, 1, 3]
harmonic_mean_3 = hmean(data2, weights=weights)
print(f"Weighted harmonic mean using scipy: {harmonic_mean_3}")