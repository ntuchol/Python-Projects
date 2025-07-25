def calculate_compound_interest(principal, rate, times_compounded, years):
    amount = principal * (1 + rate / times_compounded) ** (times_compounded * years)
    interest = amount - principal
    return amount, interest

principal = 1000  
rate = 0.05       
times_compounded = 4 
years = 5       

final_amount, interest_earned = calculate_compound_interest(principal, rate, times_compounded, years)

print(f"Final Amount: ${final_amount:.2f}")
print(f"Interest Earned: ${interest_earned:.2f}")
