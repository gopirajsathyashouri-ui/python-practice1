class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else :
            self.balance -= amount

acc = BankAccount(100)
acc.deposit(50)
print(acc.balance) 
acc.withdraw(30)
print(acc.balance)
acc.withdraw(1000) 