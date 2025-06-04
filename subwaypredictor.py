import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Load the data
data = pd.read_csv('subway_data.csv')

# Prepare the data
X = data[['time_of_day', 'day_of_week', 'previous_stop_delay']]
y = data['arrival_time']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
print(f'Mean Absolute Error: {mae}')

# Predict arrival time
new_data = pd.DataFrame({'time_of_day': [10], 'day_of_week': [3], 'previous_stop_delay': [5]})
predicted_arrival_time = model.predict(new_data)
print(f'Predicted Arrival Time: {predicted_arrival_time[0]}')