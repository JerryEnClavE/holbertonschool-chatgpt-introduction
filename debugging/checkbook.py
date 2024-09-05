class Checkbook:
    def __init__(self, overdraft_protection=True, interest_rate=0.01):
        self.balance = 0.0
        self.transactions = []
        self.overdraft_protection = overdraft_protection
        self.interest_rate = interest_rate

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
            return
        self.balance += amount
        self.transactions.append(f"Deposited: ${amount:.2f}")
        print(f"Deposited ${amount:.2f}")
        print(f"Current Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
            return
        if amount > self.balance:
            if self.overdraft_protection:
                print("Insufficient funds. Overdraft protection enabled. Transaction denied.")
                return
            else:
                self.balance -= amount
                self.transactions.append(f"Withdrew: ${amount:.2f} (Overdraft)")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew: ${amount:.2f}")
        print(f"Withdrew ${amount:.2f}")
        print(f"Current Balance: ${self.balance:.2f}")

    def get_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")

    def show_transactions(self):
        if not self.transactions:
            print("No transactions yet.")
        else:
            print("Transaction History:")
            for transaction in self.transactions:
                print(transaction)

    def apply_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        self.transactions.append(f"Applied Interest: ${interest_amount:.2f}")
        print(f"Applied ${interest_amount:.2f} interest.")
        print(f"New Balance: ${self.balance:.2f}")

def main():
    cb = Checkbook(overdraft_protection=False, interest_rate=0.02)
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, transactions, interest, exit): ").lower()
        if action == 'exit':
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif action == 'balance':
            cb.get_balance()
        elif action == 'transactions':
            cb.show_transactions()
        elif action == 'interest':
            cb.apply_interest()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
