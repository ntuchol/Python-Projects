    import numpy as np
    import matplotlib.pyplot as plt
    from scipy import stats

    # Example data
    data = np.random.normal(loc=0, scale=1, size=1000)
     # Calculate sample mean and standard error of the mean
    sample_mean = np.mean(data)
    sem = stats.sem(data) # Standard error of the mean

    # For a 90% confidence interval, the Z-score is approximately 1.645
    # (for a two-tailed test, alpha = 0.10, alpha/2 = 0.05)
    z_score = stats.norm.ppf(0.95) # Inverse of the CDF for 0.95 (1 - alpha/2)

    # Calculate the margin of error
    margin_of_error = z_score * sem

    # Calculate the confidence interval
    lower_bound = sample_mean - margin_of_error
    upper_bound = sample_mean + margin_of_error