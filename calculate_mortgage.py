def calculate_mortgage(principal, annual_rate, years):
    monthly_rate = annual_rate / 12 / 100
    total_payments = years * 12

    if monthly_rate == 0:  
        monthly_payment = principal / total_payments
    else:
        monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** total_payments) / \
                          ((1 + monthly_rate) ** total_payments - 1)

    return monthly_payment

principal = 250000  
annual_rate = 5.0   
years = 30          

monthly_payment = calculate_mortgage(principal, annual_rate, years)
print(f"Your monthly mortgage payment is: ${monthly_payment:.2f}")
