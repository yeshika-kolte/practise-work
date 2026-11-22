# 9. ATM Machine Simulation
# Problem

# Design ATM software.

# Requirements

# Each account should have:

# account number
# PIN
# balance
# Functionalities
# Login verification
# Withdraw
# Deposit
# Change PIN
# Mini statement
# Additional Challenge

# Lock account after 3 wrong PIN attempts.

# Concepts Practiced
# encapsulation mindset
# validations
# object state

class ATM :
    def __init__(self, account_number, pin, balance):
        self.__account_number = account_number
        self.__pin = pin
        self.__balance = balance

        def verify_login(self,input_pin):
            if input__pin == self.__pin and self.__account_number == account_number:
                return True 
            else:
                return False

        def withdraw(self, amount):
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew {amount}. New balance: {self.__balance}")
            else:
                print("Insufficient balance.")

        def deposit(self, amount):
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")

        def change_pin(self, old_pin, new_pin):
            if old_pin == self.__pin:
                self.__pin = new_pin
                print("PIN changed successfully.")
            else:
                print("Incorrect old PIN.")

        def mini_statement(self):
            print(f"Account Number: {self.__account_number}, Balance: {self.__balance}")


a1 = ATM("123456789", "1234", 1000)
a1.deposit(500)
a1.withdraw(200)
a1.change_pin("1234", "5678")
a1.mini_statement()


