class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional initial balance."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Deposit the specified amount into the account."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw the specified amount from the account if there are sufficient funds."""
        if amount > 0:
            if self.__account_balance >= amount:
                self.__account_balance -= amount
                return True
            else:
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """Display the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
