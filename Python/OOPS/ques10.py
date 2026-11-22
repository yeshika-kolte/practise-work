1. E-Commerce Product System
Problem

Create product system for online store.

Requirements

Each product should have:

product name
price
category
Functionalities
Apply GST using static method
Apply category discount
Display final price
Concepts Practiced
static methods
calculations
reusable logic

class Produt:
     def__init__(self , product_name , price , category):
        self.__product_name = product_name
        self.__price = price
        self.__category = category

    @staticmethod
    def apply_gst(price ,gst):
        return price +(price *gst/100)

    def category_discount(self ,discount):
        if self.__category == "crocery":
            self.__price -= self.__price *(discount/100)

    def display_final_price(self):
        final_price = self.apply_gst(self.__price , 18)
        print(f"Final price of {self.__product_name} after GST: {final_price}")
        
