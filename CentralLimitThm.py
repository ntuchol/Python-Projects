    import numpy as np
    import matplotlib.pyplot as plt

    # Simulate data from a non-normal distribution (e.g., exponential)
    population = np.random.exponential(scale=2, size=10000)

    sample_means = []
    num_samples = 1000
    sample_size = 30 # A common threshold for "large enough"

    for _ in range(num_samples):
        sample = np.random.choice(population, size=sample_size, replace=True)
        sample_means.append(np.mean(sample))

    plt.hist(sample_means, bins=30, density=True, alpha=0.7, color='skyblue')
    plt.title('Distribution of Sample Means (CLT Demonstration)')
    plt.xlabel('Sample Mean')
    plt.ylabel('Frequency')
    plt.show()