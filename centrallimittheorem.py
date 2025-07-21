import numpy as np
import matplotlib.pyplot as plt

# 1. Generate a non-normal population (e.g., uniform distribution)
population = np.random.uniform(0, 100, 10000)

# Parameters for sampling
sample_size = 30
num_samples = 1000

# 2. & 3. Repeatedly draw samples and calculate means
sample_means = []
for _ in range(num_samples):
    sample = np.random.choice(population, sample_size)
    sample_means.append(np.mean(sample))

# 4. Visualize the distribution of sample means
plt.hist(sample_means, bins=30, edgecolor='black')
plt.title('Distribution of Sample Means (Central Limit Theorem)')
plt.xlabel('Sample Mean')
plt.ylabel('Frequency')
plt.show()