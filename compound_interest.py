def compound_interest(principal, rate, time, n):
    """
    Calculates compound interest.

    Args:
        principal: The principal amount.
        rate: The annual interest rate (as a decimal).
        time: The time in years.
        n: The number of times interest is compounded per year.

    Returns:
        The future value of the investment/loan.
    """
    amount = principal * (1 + (rate / n))**(n * time)
    return amount

# Example usage
principal = 1000
rate = 0.05
time = 5
n = 12  # monthly compounding

future_value = compound_interest(principal, rate, time, n)
print("The future value is:", future_value)

compound_interest_only = future_value - principal
print("The compound interest earned is:", compound_interest_only)