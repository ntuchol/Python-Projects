def rule_of_72(interest_rate):
    
    if interest_rate <= 0:
        return "Interest rate must be greater than 0."
    return 72 / interest_rate

rate = 6  
years = rule_of_72(rate)
print(f"At an interest rate of {rate}%, it will take approximately {years:.2f} years to double your investment.")
