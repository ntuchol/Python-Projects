import pandas as pd

    temperatures = [25, 28, 21, 30, 26]
    max_temperature = max(temperatures)
    print(max_temperature)  
    
 weather_data = [
        {'city': 'A', 'temperature': 25},
        {'city': 'B', 'temperature': 30},
        {'city': 'C', 'temperature': 22}
    ]
    max_temp_city = max(weather_data, key=lambda x: x['temperature'])
    print(max_temp_city)  

    data = {'date': ['2024-05-01', '2024-05-02', '2024-05-03'],
            'temperature': [25, 28, 31]}
    df = pd.DataFrame(data)
    max_temp = df['temperature'].max()
    print(max_temp) # Output: 31

    dates = pd.to_datetime(['2024-05-01 12:00:00', '2024-05-01 18:00:00', '2024-05-02 12:00:00'])
    temps = [20, 25, 30]
    df = pd.DataFrame({'TIMESTAMP': dates, 'temperature': temps})
    daily_max = df.resample('1D', on='TIMESTAMP')['temperature'].max()
    print(daily_max)
