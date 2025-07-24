import seaborn as sns
import matplotlib.pyplot as plt

    # Load a sample dataset (e.g., Iris dataset)
    iris = sns.load_dataset("iris")

    # Create a basic pairplot
    sns.pairplot(iris)
    plt.show()

    # Create a pairplot with hue and custom diagonal kind
    sns.pairplot(iris, hue="species", diag_kind="kde")
    plt.show()