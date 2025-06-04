def calculate_compound_interest(principal, rate, times_compounded, years):
    # Calculate the final amount
    amount = principal * (1 + rate / times_compounded) ** (times_compounded * years)
    # Calculate the interest earned
    interest = amount - principal
    return amount, interest

# Example usage
principal = 1000  # Initial investment ($)
rate = 0.05       # Annual interest rate (5%)
times_compounded = 4  # Quarterly compounding
years = 5         # Investment duration in years

final_amount, interest_earned = calculate_compound_interest(principal, rate, times_compounded, years)

print(f"Final Amount: ${final_amount:.2f}")
print(f"Interest Earned: ${interest_earned:.2f}")