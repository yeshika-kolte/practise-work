# 16. E-commerce User Roles
# User
# Seller(User)
# PremiumSeller(Seller)

# Add premium benefits.

class User:
    def __init__(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

class Seller(User):
    def __init__(self,name,sell_id,product):
        super().__init__(name)
        self.__seller_id = sell_id
        self.__product = product

    def get_sellerId(self):
        return self.__seller_id
    
    def get_product(self):
        return self.__product
    
class PremiuimSeller(Seller):
    def __init__(self,name,sell_id,product,maxProfit):
        super().__init__(name,sell_id,product)
        self.__maxProfit = maxProfit

    def display(self):
        print("-------Seller Detail-------")
        print(f"Seller Name :{self.get_name()}")
        print(f"Seller Id : {self.get_sellerId()}")
        print(f"Seller Product : {self.get_product()}")

    def benefit(self):
        print(f"You have profit of {self.__maxProfit}% in each selling product")


ps = PremiuimSeller("Rahul","201","Smartphone",20)
ps.display()
ps.benefit()
