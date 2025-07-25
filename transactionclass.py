class Transaction:
    def __init__(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        self.amount = amount

    def __str__(self):
        return f"Transaction(amount={self.amount})"

    def apply_discount(self, percentage):
        if not (0 <= percentage <= 100):
            raise ValueError("Percentage must be between 0 and 100.")
        self.amount -= self.amount * (percentage / 100)

    def add_tax(self, percentage):
        if not (0 <= percentage <= 100):
            raise ValueError("Percentage must be between 0 and 100.")
        self.amount += self.amount * (percentage / 100)

try:
    transaction = Transaction(100)
    print(transaction)  

    transaction.apply_discount(10)  
    print(transaction) 

    transaction.add_tax(5)  
    print(transaction)  
except ValueError as e:
    print(f"Error: {e}")
