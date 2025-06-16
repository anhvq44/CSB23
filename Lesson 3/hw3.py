class MainAccount:
    def __init__(self, account_id, name, balance=0):
        self.account_id = account_id
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Not enough money.")

class SavingAccount(MainAccount):
    def __init__(self, account_id, name, interest_rate, balance=0):
        super().__init__(account_id, name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: {interest}. New balance: {self.balance}")