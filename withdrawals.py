class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient funds"

#Example Usage
account = BankAccount(100)
print("Current balance:", account.balance)

account.deposit(50)
print("Balance after deposit:", account.balance)

withdrawal_amount = 20
result = account.withdraw(withdrawal_amount)
if isinstance(result, str):
    print(result)
else:
    print(f"Withdrawal of ${withdrawal_amount} successful. New balance: ${result}")

withdrawal_amount = 200
result = account.withdraw(withdrawal_amount)
if isinstance(result, str):
    print(result)
else:
    print(f"Withdrawal of ${withdrawal_amount} successful. New balance: ${result}")