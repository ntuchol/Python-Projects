import seaborn as sns
df = sns.load_dataset("anscombe")

import matplotlib.pyplot as plt

    sns.lmplot(
        data=df,
        x="x",
        y="y",
        col="dataset",  
        hue="dataset",  
        col_wrap=2,     
        ci=None,       
        height=4,
        scatter_kws={"s": 50, "alpha": 1} 
    )
    plt.suptitle("Anscombe's Quartet", y=1.02) 
    plt.show()


