class Wallet:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance

    def get_owner(self):
        return self.__owner

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

class Transaction:
    def __init__(self, wallet):
        self.__wallet = wallet

    def deposit(self, amount):
        new_balance = self.__wallet.get_balance() + amount
        self.__wallet.set_balance(new_balance)
        print(f"Deposited : {amount}")
        print(f"Balance : {self.__wallet.get_balance()}")

    def withdraw(self, amount):
        if self.__wallet.get_balance() >= amount:
            new_balance = self.__wallet.get_balance() - amount
            self.__wallet.set_balance(new_balance)
            print(f"Withdrawn : {amount}")
            print(f"Balance : {self.__wallet.get_balance()}")
        else:
            print("Insufficient Balance")

obj1 = Wallet("Rahul", 50000)
obj2 = Transaction(obj1)
obj2.deposit(10000)
obj2.withdraw(20000)