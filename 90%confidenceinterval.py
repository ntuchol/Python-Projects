    import numpy as np
    import matplotlib.pyplot as plt
    from scipy import stats

    data = np.random.normal(loc=0, scale=1, size=1000)
    sample_mean = np.mean(data)
    sem = stats.sem(data) 
    z_score = stats.norm.ppf(0.95) 
    margin_of_error = z_score * sem
    lower_bound = sample_mean - margin_of_error
    upper_bound = sample_mean + margin_of_error
