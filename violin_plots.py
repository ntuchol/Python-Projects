import seaborn as sns
    import matplotlib.pyplot as plt

    # Load example dataset
    tips = sns.load_dataset("tips")

    # Create a simple violin plot
    sns.violinplot(x="day", y="total_bill", data=tips)
    plt.show()
    # Generate some sample data
    data = [np.random.normal(0, std, 100) for std in range(1, 4)]

    # Create a violin plot
    plt.violinplot(data)
    plt.show()
    import plotly.express as px

    # Load example dataset
    df = px.data.tips()

    # Create an interactive violin plot
    fig = px.violin(df, x="day", y="tip")
    fig.show()