def interest_only_mortgage(loan_amount, annual_interest_rate, months):
    """
    Calculate monthly interest-only mortgage payments.

    :param loan_amount: Total loan amount (principal)
    :param annual_interest_rate: Annual interest rate (as a percentage, e.g., 5 for 5%)
    :param months: Number of months for the interest-only period
    :return: Monthly interest payment
    """
    # Convert annual interest rate to a monthly rate (decimal form)
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    
    # Calculate monthly interest payment
    monthly_payment = loan_amount * monthly_interest_rate
    
    return monthly_payment

# Example usage
loan_amount = 300000  # Loan amount in dollars
annual_interest_rate = 5  # Annual interest rate in percentage
months = 60  # Interest-only period in months

monthly_payment = interest_only_mortgage(loan_amount, annual_interest_rate, months)
print(f"Monthly interest-only payment: ${monthly_payment:.2f}")
