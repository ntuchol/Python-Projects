def interest_only_mortgage(loan_amount, annual_interest_rate, months):
    
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    
    monthly_payment = loan_amount * monthly_interest_rate
    
    return monthly_payment

loan_amount = 300000  
annual_interest_rate = 5  
months = 60  

monthly_payment = interest_only_mortgage(loan_amount, annual_interest_rate, months)
print(f"Monthly interest-only payment: ${monthly_payment:.2f}")
