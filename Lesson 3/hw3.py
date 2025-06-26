class MainAccount:
    def __init__(self, account_id, name, balance=0):
        self.account_id = account_id
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}VND")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}VND")
        else:
            print("Not enough money.")

class SavingAccount(MainAccount):
    def __init__(self, account_id, name, interest_rate, balance=0):
        super().__init__(account_id, name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: {interest}. New balance: {self.balance}VND")
        
def main():
    main_acc_1 = MainAccount("001", "Nguyen Minh Tam", 10000000)
    main_acc_2 = MainAccount("002", "Pham Duc Hung", 123456789)
    save_acc_3 = SavingAccount("003", "Vu Minh Huy", interest_rate=0.05, balance=999000)
    main_acc_4 = MainAccount("004", "Dang Dinh Nam", 9000)
    
    main_acc_1.deposit(1000000)
    main_acc_2.withdraw(23000000)
    save_acc_3.deposit(23000000)
    save_acc_3.add_interest()
    main_acc_4.withdraw(123456)
    
main()