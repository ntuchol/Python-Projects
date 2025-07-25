def calculate_future_value(present_value, annual_rate, years):
    
    future_value = present_value * (1 + annual_rate) ** years
    return future_value

present_value = 1000  
annual_rate = 0.05    
years = 10            

future_value = calculate_future_value(present_value, annual_rate, years)
print(f"The future value of the investment is: ${future_value:.2f}")
