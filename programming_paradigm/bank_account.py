class bank_account:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance
    def deposit(self, amount):
        self.account_balance += amount
    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
        else:
            print("Insufficient funds")
            return True
        return False
    def display_balance(self):
        print(f"current balance is {self.account_balance}")
