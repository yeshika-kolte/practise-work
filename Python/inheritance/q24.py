# 24. ATM System

# Abstract:

# ATM

# Derived:

# SBIATM
# HDFCATM

# Implement banking operations.

from abc import *
class ATM(ABC):
    @abstractmethod
    def credit(self):
        pass
    
    @abstractmethod
    def debit(self):
        pass
    
    @abstractmethod
    def balance_check():
        pass
    
    @abstractmethod
    def statement():
        pass

class SBIATM:
    def __init__(self,card_no,pin,balance):
        self.__card_no=card_no
        self.__balance = balance
        self.__pin = pin

    def debit(self,amount):
        self.__balance -= amount
        print("Amount debited")
        print(f"Balance : {self.__balance}")
        
    def credit(self,amount):
        self.__balance+=amount
        print("Amount credited")
        print(f"Balance : {self.__balance}")

    def statement(self):
        print("-------Statement - SBI Bank-------")
        print(f"Account Numeber :{self.__card_no}")
        print(f"Balance : {self.__balance}")


class HDFC:
    def __init__(self,card_no,pin,balance):
        self.__card_no=card_no
        self.__balance = balance
        self.__pin = pin

    def debit(self,amount):
        self.__balance -= amount
        print("Amount debited")
        
    def credit(self,amount):
        self.__balance+=amount

    def statement(self):
        print("-------Statement - HDFC Bank-------")
        print(f"Account Numeber :{self.__card_no}")
        print(f"Balance : {self.__balance}")


sbi = SBIATM(12312312,1234,900000)
sbi.debit(1000)
sbi.credit(10000)
sbi.statement()


