class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited:", amount)
        print("New Balance:", self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            print("Withdrew:", amount)
        else:
            print("Insufficient Balance")
    
    def display_balance(self):
        print("User:", self.account_holder)
        print("Balance:", self.balance)


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate 

    def add_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance = self.balance + interest
        print("Interest added:", interest)
        print("Final Savings Balance:", self.balance)


class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit 

    def withdraw_with_overdraft(self, amount):
        if (self.balance + self.overdraft_limit) >= amount:
            self.balance = self.balance - amount
            print("Overdraft Withdrawal Successful.")
            print("New Balance:", self.balance)
        else:
            print("Overdraft Limit Exceeded!")


print("\n--- SAVINGS ACCOUNT DEMO ---")
savings_user = SavingsAccount("Raj", 1000, 5) 
savings_user.deposit(500)      
savings_user.add_interest()    

print("\n--- CURRENT ACCOUNT DEMO ---")
current_user = CurrentAccount("Sam", 2000, 1000)
current_user.withdraw_with_overdraft(2500) 