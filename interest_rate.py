def calculate_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest

# Example usage
principal = 1000  # Principal amount in dollars
rate = 5          # Annual interest rate in percentage
time = 2          # Time in years

si = calculate_simple_interest(principal, rate, time)
print(f"Simple Interest: ${si:.2f}")