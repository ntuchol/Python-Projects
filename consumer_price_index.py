import pandas as pd

data = {
    "Year": [2020, 2021, 2022],
    "Good_A": [50, 55, 60],
    "Good_B": [30, 35, 40],
    "Good_C": [20, 25, 30]
}

df = pd.DataFrame(data)

df["Basket_Cost"] = df[["Good_A", "Good_B", "Good_C"]].sum(axis=1)

base_year_cost = df.loc[df["Year"] == 2020, "Basket_Cost"].values[0]
df["CPI"] = (df["Basket_Cost"] / base_year_cost) * 100

print(df)
