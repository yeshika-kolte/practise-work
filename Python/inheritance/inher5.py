# 5. Banking System
# Parent:
# BankAccount
# Child:
# SavingsAccount
# CurrentAccount
# Implement withdrawal rules.

class BankAccount:
    def __init__(self, acc_no, holder, balance=0):
        self.__acc_no = acc_no
        self.__holder = holder
        self.__balance = balance

    def get_acc_no(self):
        return self.__acc_no

    def get_holder(self):
        return self.__holder

    def get_balance(self):
        return self.__balance

    def withdraw(self, amount):
        print("Withdrawal rule not defined")


class SavingsAccount(BankAccount):
    def __init__(self, acc_no, holder, balance=0, min_balance=1000):
        super().__init__(acc_no, holder, balance)
        self.__min_balance = min_balance

    def withdraw(self, amount):
        if self.get_balance() - amount >= self.__min_balance:
            self._BankAccount__balance = self.get_balance() - amount
            print("Savings withdrawal:", amount)
        else:
            print("Denied: Minimum balance rule")


class CurrentAccount(BankAccount):
    def __init__(self, acc_no, holder, balance=0, overdraft=5000):
        super().__init__(acc_no, holder, balance)
        self.__overdraft = overdraft

    def withdraw(self, amount):
        if self.get_balance() - amount >= -self.__overdraft:
            self._BankAccount__balance = self.get_balance() - amount
            print("Current withdrawal:", amount)
        else:
            print("Denied:  limit exceeded")



s = SavingsAccount("101", "Ishika", 5000)
c = CurrentAccount("201", "Rahul", 2000)

s.withdraw(3500)  
c.withdraw(6000)   
