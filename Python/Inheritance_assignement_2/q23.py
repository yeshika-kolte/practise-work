class BankAccount:
    def __init__(self , name, balance):
        self.__name = name
        self.__balance = balance

    def withdraw(self, amount):
        pass

    def get_name(self):
        return self.__name
    
    def get_balace(self):
        return self.__balance

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if self.get_balace()  >= amount:
            new_balance = self.get_balace() - amount
            print(f"Amt {amount} withdraw from SA")
            print(f"Balance : {new_balance}")
        else:
            print("err")

class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        if self.get_balace()  >= amount:
            new_balance =self.get_balace()- amount
            print(f"Amt {amount} withdraw from CA")
            print(f"Balance : {new_balance}")
        else:
            print("err")

# obj1 = SavingsAccount("Rahul", 11000)
# obj1.withdraw(8000)
obj2 = CurrentAccount("Siaa", 20000)
obj2.withdraw(3000)