import pandas as pd

# Example data: prices of goods over time
data = {
    "Year": [2020, 2021, 2022],
    "Good_A": [50, 55, 60],
    "Good_B": [30, 35, 40],
    "Good_C": [20, 25, 30]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate the total cost of the basket for each year
df["Basket_Cost"] = df[["Good_A", "Good_B", "Good_C"]].sum(axis=1)

# Set the base year (e.g., 2020) and calculate CPI
base_year_cost = df.loc[df["Year"] == 2020, "Basket_Cost"].values[0]
df["CPI"] = (df["Basket_Cost"] / base_year_cost) * 100

# Display the results
print(df)