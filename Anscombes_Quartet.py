import seaborn as sns
df = sns.load_dataset("anscombe")

import matplotlib.pyplot as plt

    sns.lmplot(
        data=df,
        x="x",
        y="y",
        col="dataset",  # Create separate plots for each dataset
        hue="dataset",  # Color points based on dataset
        col_wrap=2,     # Wrap plots into two columns
        ci=None,        # Do not show confidence interval for regression line
        height=4,
        scatter_kws={"s": 50, "alpha": 1} # Customize scatter plot points
    )
    plt.suptitle("Anscombe's Quartet", y=1.02) # Add a main title
    plt.show()


