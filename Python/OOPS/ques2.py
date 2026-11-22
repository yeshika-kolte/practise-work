class Bank_Account:
    interest_rate = 7

    def __init__(self ,account_number ,account_holder ,balance):
        self.account_number = account_number
        self.account_holder = account_holder    
        self.balance = balance
    def deposit(self ,amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount")    
    def withdraw(self ,amount): 
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdraw amount or insufficient balance")
    def display_summary(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")
        print(f"Interest Rate: {Bank_Account.interest_rate}%")

    @staticmethod
    def minimum_balance():
        return 1000

account1 = Bank_Account("1234567890","anushka", 5000)
account1.deposit(2000)
account1.withdraw(1500)
account1.display_summary()
print("Minimum Balance:", Bank_Account.minimum_balance())

