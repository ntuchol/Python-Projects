import random

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.account_number = self.generate_account_number()
        self.balance = balance
        self.transaction_history = []

    def generate_account_number(self):
         return ''.join(random.choices('0123456789', k=5))
    
    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: +{amount}")
        print("Deposit successful.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawn: -{amount}")
            print("Withdrawal successful.")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def get_transaction_history(self):
         for transaction in self.transaction_history:
              print(transaction)

    def __str__(self):
        return f"Account Number: {self.account_number}, Account Holder Name: {self.name}, Balance: {self.balance}"

# Example usage
account1 = BankAccount("Alice", 1000)
print(account1)
account1.deposit(500)
account1.withdraw(200)
account1.check_balance()
account1.get_transaction_history()