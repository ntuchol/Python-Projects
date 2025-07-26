import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

sns.pairplot(iris)
plt.show()

sns.pairplot(iris, hue="species", diag_kind="kde")
plt.show()
