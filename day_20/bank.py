

class Bank:

    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):

        self.balance = self.balance + amount
        print(f"{self.balance}")

    def withdraw(self, amount):

        if amount < self.balance:
            self.balance = self.balance - amount
            print(f"{self.balance}")

        else:
            print("Insufficient Balance")

    def get_balance(self):
        print(f"{self.balance}")


my_account = Bank(0)

my_account.deposit(1000)

my_account.withdraw(100)

my_account.get_balance()