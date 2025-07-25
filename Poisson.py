import numpy as np

lam_value = 5

rng = np.random.default_rng()
poisson_samples = rng.poisson(lam=lam_value, size=4000)

print("First 10 Poisson samples:", poisson_samples[:10])

print("Mean of generated samples:", np.mean(poisson_samples))
