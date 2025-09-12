class BankAccount:
    def __init__(self,balance=0):
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        
    def withdraw(self,amount):
        self.amount=amount
        if self.balance>=self.amount:
            self.balance-=self.amount
        else:
            print("no sufficient money")
    def get_balance(self):
        
        print("final balance:",self.balance)
ob=BankAccount()
ob.deposit(5000)
ob.withdraw(2000)
ob.get_balance()

    
    

