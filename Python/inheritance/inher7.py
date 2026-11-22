# 7. Shopping Cart System
# Base:
# Product
# Derived:
# Electronics
# Grocery
# Clothing
# Apply discounts.


class Product():
    def __init__(self, pro_id, pro_name , price):
        self.__pro_id =pro_id
        self.__pro_name = pro_name
        self.__price =price
    
    def get_pro_id(self):
        return self.__pro_id

    def get_pro_name(self):
        return self.__pro_name

    def get_price(Self):
        return self.__price 
    
    def apply_discount(self):
        print("no dicount applied")

class Electronics(Product):
    def apply_discount(self):
        discounted = self.get_price() * 0.90  
        print("Electronics discounted price:", discounted)

class Grocery(Product):
     def apply_discount(self):
        dicounted =self.get_price()*0.85
        print("Grocery discounted price:",discounted)

class Clothing(Product):
     def apply_discount(self):
        dicounted =self.get_price()*0.80
        print("clothing dicount price:",discounted)

e=Electronics("101","phone","200000")  
g=Grocery("102","semolina","120") 
c=Clothing("103","top","5000")  

print(e.get_pro_name())
e.apply_discount()

print(g.get_pro_name())
g.apply_discount()

print(c.get_pro_name())
c.apply_discount()