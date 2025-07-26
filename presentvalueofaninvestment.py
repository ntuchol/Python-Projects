def calculate_present_value(future_value, discount_rate, periods):
    
    present_value = future_value / ((1 + discount_rate) ** periods)
    return present_value

future_value = 10000  
discount_rate = 0.05  
periods = 10        

pv = calculate_present_value(future_value, discount_rate, periods)
print(f"The present value of the investment is: ${pv:.2f}")
