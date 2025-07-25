def compound_interest(principal, rate, time, n):
    amount = principal * (1 + (rate / n))**(n * time)
    return amount

principal = 1000
rate = 0.05
time = 5
n = 12  

future_value = compound_interest(principal, rate, time, n)
print("The future value is:", future_value)

compound_interest_only = future_value - principal
print("The compound interest earned is:", compound_interest_only)
