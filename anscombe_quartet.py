import seaborn as sns
df = sns.load_dataset("anscombe")

import matplotlib.pyplot as plt
    sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=df,
               col_wrap=2, ci=None, palette="muted", height=4)
    plt.show()