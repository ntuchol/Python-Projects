class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} deposited successfully!")
        else:
            print("Invalid deposit amount. Please try again.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Please try a smaller amount.")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please try again.")
        else:
            self.balance -= amount
            print(f"${amount:.2f} withdrawn successfully!")

def atm_menu():
    atm = ATM(balance=1000)  
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            try:
                amount = float(input("Enter amount to deposit: "))
                atm.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw: "))
                atm.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    atm_menu()
