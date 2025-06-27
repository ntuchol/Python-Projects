def calculate_mortgage(principal, annual_rate, years):
    # Convert annual rate to monthly and years to months
    monthly_rate = annual_rate / 12 / 100
    total_payments = years * 12

    # Mortgage formula
    if monthly_rate == 0:  # Handle zero interest rate
        monthly_payment = principal / total_payments
    else:
        monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** total_payments) / \
                          ((1 + monthly_rate) ** total_payments - 1)

    return monthly_payment


# Example usage
principal = 250000  # Loan amount in dollars
annual_rate = 5.0   # Annual interest rate in percent
years = 30          # Loan term in years

monthly_payment = calculate_mortgage(principal, annual_rate, years)
print(f"Your monthly mortgage payment is: ${monthly_payment:.2f}")