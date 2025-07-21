import numpy as np

# Set the lambda (mean) for the Poisson distribution
lam_value = 5

# Generate 4000 random samples from the Poisson distribution
# using the default_rng() for modern random number generation
rng = np.random.default_rng()
poisson_samples = rng.poisson(lam=lam_value, size=4000)

# Print the first few samples to verify
print("First 10 Poisson samples:", poisson_samples[:10])

# Print the mean of the generated samples (should be close to lam_value)
print("Mean of generated samples:", np.mean(poisson_samples))