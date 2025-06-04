import pandas as pd

# Load the dataset
alcohol = pd.read_csv('world_alcohol.csv')

# Rename columns for easier use
alcohol.rename(columns={'Year': 'year', 'WHO region': 'who_region', 'Country': 'country',
                        'Beverage Types': 'beverage_types', 'Display Value': 'display_value'}, inplace=True)

# Handle missing values by dropping rows with NaN
alcohol_cleaned = alcohol.dropna()

# Calculate mean wine consumption per continent
wine_consumption = alcohol_cleaned[alcohol_cleaned['beverage_types'] == 'Wine'].groupby('who_region')['display_value'].mean()

print("Mean wine consumption per region:\n", wine_consumption)

# Find average consumption of wine per person greater than 2
average_wine_consumption = alcohol_cleaned[alcohol_cleaned['beverage_types'] == 'Wine']
average_wine_consumption = average_wine_consumption[average_wine_consumption['display_value'] > 2]

print("\nAverage wine consumption greater than 2:\n", average_wine_consumption)

# Display the shape of the dataset
print("\nShape of the dataset:", alcohol.shape)