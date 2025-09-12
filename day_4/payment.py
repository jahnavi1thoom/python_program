class Payment:
    def pay(self,amount):
        print("paid ₹",amount)
class CashPayment(Payment):
    
    def pay(self,amount):
        print("paid ₹",amount,"in cash")
class CardPayment(Payment):
    
    def pay(self,amount):
        print("Paid ₹",amount,"using credit/debit card")
class UPIPayment(Payment):
   
    def pay(self,amount):
        print("Paid ₹",amount,"using UPI")
payments=[CashPayment(),CardPayment(),UPIPayment()]
for p in payments:
    p.pay(1000)
