import pandas as pd

alcohol = pd.read_csv('world_alcohol.csv')

alcohol.rename(columns={'Year': 'year', 'WHO region': 'who_region', 'Country': 'country',
                        'Beverage Types': 'beverage_types', 'Display Value': 'display_value'}, inplace=True)

alcohol_cleaned = alcohol.dropna()

wine_consumption = alcohol_cleaned[alcohol_cleaned['beverage_types'] == 'Wine'].groupby('who_region')['display_value'].mean()

print("Mean wine consumption per region:\n", wine_consumption)

average_wine_consumption = alcohol_cleaned[alcohol_cleaned['beverage_types'] == 'Wine']
average_wine_consumption = average_wine_consumption[average_wine_consumption['display_value'] > 2]

print("\nAverage wine consumption greater than 2:\n", average_wine_consumption)

print("\nShape of the dataset:", alcohol.shape)
