import seaborn as sns
    import matplotlib.pyplot as plt

    tips = sns.load_dataset("tips")

    sns.violinplot(x="day", y="total_bill", data=tips)
    plt.show()
    data = [np.random.normal(0, std, 100) for std in range(1, 4)]

    plt.violinplot(data)
    plt.show()
    import plotly.express as px

    df = px.data.tips()

    fig = px.violin(df, x="day", y="tip")
    fig.show()
