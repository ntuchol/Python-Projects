class Transaction:
    def __init__(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        self.amount = amount

    def __str__(self):
        return f"Transaction(amount={self.amount})"

    def apply_discount(self, percentage):
        """Apply a discount to the transaction amount."""
        if not (0 <= percentage <= 100):
            raise ValueError("Percentage must be between 0 and 100.")
        self.amount -= self.amount * (percentage / 100)

    def add_tax(self, percentage):
        """Add tax to the transaction amount."""
        if not (0 <= percentage <= 100):
            raise ValueError("Percentage must be between 0 and 100.")
        self.amount += self.amount * (percentage / 100)

# Example usage:
try:
    transaction = Transaction(100)
    print(transaction)  # Output: Transaction(amount=100)

    transaction.apply_discount(10)  # Apply 10% discount
    print(transaction)  # Output: Transaction(amount=90.0)

    transaction.add_tax(5)  # Add 5% tax
    print(transaction)  # Output: Transaction(amount=94.5)
except ValueError as e:
    print(f"Error: {e}")