# 19. Mobile Phone Hierarchy
# Phone
# Smartphone
# AndroidPhone

# Add Android features.

class Phone:
    def __init__(self,name,price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name
    def get_prices(self):
        return self.__price
    
class Smartphone(Phone):
    def __init__(self,name,price,brand):
        super().__init__(name,price)
        self.__brand = brand
    
    def get_brand(self):
        return self.__brand
    
class AndroidPhone(Smartphone):
    def __init__(self, name, price, brand,version):
        super().__init__(name, price, brand)
        self.__version = version

    def call_received(self):
        print("Call received ...")

    def call_cut(self):
        print("Call Cut....")
    
    def detail(self):
        print(f"Name : {self.get_name()}")
        print(f"Price : {self.get_prices()}")
        print(f"Brand : {self.get_brand()}")
        print(f"Version : {self.__version}")


ap = AndroidPhone("Samsung S25 Ultra",150000,"Samsung","16")

ap.detail()