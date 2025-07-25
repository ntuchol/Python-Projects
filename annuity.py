def present_value_annuity(payment, interest_rate, periods):
    
    if interest_rate == 0:  
        return payment * periods
    return payment * (1 - (1 + interest_rate) ** -periods) / interest_rate

payment = 1000  
interest_rate = 0.05  
periods = 10 
pv = present_value_annuity(payment, interest_rate, periods)
print(f"The present value of the annuity is: ${pv:.2f}")
