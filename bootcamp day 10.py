class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Welcome to Deposite and Withdrawal Machine")
    
class deposit(Bank_Account):
    def deposit(self):
        Amount=float(input("Enter the amount to be deposited:"))
        self.balance = self.balance + Amount
        print("Amount Deposited",Amount)
    def withdraw(self):
        Amount=float(input("Enter the amount to be withdrawed"))
        self.balance >=Amount
        self.balance =self.balance-Amount
        print("Amount withdrawed",Amount)
    def display(self):    
        print("Net balance",self.balance)
    
a=deposit()
a.deposit()
a.withdraw()
a.display()

