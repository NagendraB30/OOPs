class Payment:
    def pay(self):
        print("Processing generic payment...")

class GooglePay(Payment):
    def pay(self):
        print("Payment successful using Google Pay.")

class PhonePe(Payment):
    def pay(self):
        print("Payment successful using PhonePe.")

class CreditCard(Payment):
    def pay(self):
        print("Payment successful using Credit Card.")

gp = GooglePay()
pp = PhonePe()
cc = CreditCard()

gp.pay()
pp.pay()
cc.pay()