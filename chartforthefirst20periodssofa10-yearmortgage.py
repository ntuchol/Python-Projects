import matplotlib.pyplot as plt
import numpy as np

loan_amount = 200000  
annual_interest_rate = 5.0  
years = 10  
periods = years * 12  
monthly_interest_rate = annual_interest_rate / 100 / 12

monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** periods) / \
                  ((1 + monthly_interest_rate) ** periods - 1)

principal_remaining = loan_amount
principal_paid = []
interest_paid = []
balances = []

for i in range(1, 21):
    interest = principal_remaining * monthly_interest_rate
    principal = monthly_payment - interest
    principal_remaining -= principal

    interest_paid.append(interest)
    principal_paid.append(principal)
    balances.append(principal_remaining)

plt.figure(figsize=(10, 6))
plt.plot(range(1, 21), interest_paid, label="Interest Paid", marker='o')
plt.plot(range(1, 21), principal_paid, label="Principal Paid", marker='o')
plt.plot(range(1, 21), balances, label="Remaining Balance", marker='o')

plt.title("Mortgage Breakdown for First 20 Periods")
plt.xlabel("Payment Period")
plt.ylabel("Amount ($)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
