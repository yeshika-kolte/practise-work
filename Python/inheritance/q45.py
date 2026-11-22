class Menu:
    def __init__(self, item, price):
        self.__item = item
        self.__price = price

    def get_item(self):
        return self.__item

    def get_price(self):
        return self.__price

class Order:
    def __init__(self, menu, quantity):
        self.__menu = menu
        self.__quantity = quantity

    def get_quantity(self):
        return self.__quantity

    def total_bill(self):
        return self.__menu.get_price() * self.__quantity

    def display_order(self):
        print(f"Item : {self.__menu.get_item()}")
        print(f"Quantity : {self.get_quantity()}")
        print(f"Bill : {self.total_bill()}")

class Payment:
    def pay(self, amount):
        print(f"Payment Done : {amount}")

class Discount:
    def apply_discount(self, amount, percent):
        final = amount - ((amount * percent) / 100)
        return final

m1 = Menu("Pizza", 250)
o1 = Order(m1, 2)
o1.display_order()
total = o1.total_bill()
d1 = Discount()
final_amount = d1.apply_discount(total, 10)
print(f"Final Amount After Discount : {final_amount}")
p1 = Payment()
p1.pay(final_amount)