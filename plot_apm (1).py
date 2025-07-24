import matplotlib.pyplot as plt
    import numpy as np
     # Example: Generate random APM data (replace with your actual data)
    apm_data = np.random.normal(loc=150, scale=30, size=1000)
    # loc is the mean, scale is the standard deviation, size is the number of data points
plt.hist(apm_data, bins=20, edgecolor='black', alpha=0.7)
    # apm_data: The data to plot.
    # bins: The number of bins or a sequence of bin edges.
    # edgecolor: Color of the bin edges for better visualization.
    # alpha: Transparency of the bars (0.0 to 1.0).
plt.xlabel("APM (Actions Per Minute)")
    plt.ylabel("Frequency")
    plt.title("Distribution of APM")
        plt.show()
