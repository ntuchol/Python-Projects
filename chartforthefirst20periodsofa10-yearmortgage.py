import matplotlib.pyplot as plt
import numpy as np

# Mortgage parameters
loan_amount = 200000  # Example loan amount in dollars
annual_interest_rate = 5.0  # Annual interest rate in percent
years = 10  # Loan term in years
periods = years * 12  # Total number of monthly payments

# Convert annual interest rate to monthly interest rate
monthly_interest_rate = annual_interest_rate / 100 / 12

# Calculate monthly payment using the loan amortization formula
monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** periods) / \
                  ((1 + monthly_interest_rate) ** periods - 1)

# Initialize lists to store data for the first 20 periods
principal_remaining = loan_amount
principal_paid = []
interest_paid = []
balances = []

# Calculate breakdown for the first 20 periods
for i in range(1, 21):
    interest = principal_remaining * monthly_interest_rate
    principal = monthly_payment - interest
    principal_remaining -= principal

    interest_paid.append(interest)
    principal_paid.append(principal)
    balances.append(principal_remaining)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(range(1, 21), interest_paid, label="Interest Paid", marker='o')
plt.plot(range(1, 21), principal_paid, label="Principal Paid", marker='o')
plt.plot(range(1, 21), balances, label="Remaining Balance", marker='o')

# Add labels and legend
plt.title("Mortgage Breakdown for First 20 Periods")
plt.xlabel("Payment Period")
plt.ylabel("Amount ($)")
plt.legend()
plt.grid(True)

# Show the chart
plt.tight_layout()
plt.show()