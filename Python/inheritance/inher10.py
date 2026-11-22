

class Ticket:
    def __init__(self, movie_name, num_of_tickets, price):
        self.__movie_name = movie_name
        self.__num_of_tickets = num_of_tickets
        self.__price = price

    def get_movie_name(self):
        return self.__movie_name

    def get_num_of_tickets(self):
        return self.__num_of_tickets

    def get_price(self):
        return self.__price

    def calculate_price(self):
        return self.__num_of_tickets * self.__price


class GoldTicket(Ticket):
    def final_price(self):
        extra_charge = 1000
        total = self.calculate_price() + extra_charge
        return total

class PlatinumTicket(Ticket):
    def final_price(self):
        extra_charge = 500
        total = self.calculate_price() + extra_charge
        return total

class VIPTicket(Ticket):
    def final_price(self):
        extra_charge = 2000
        total = self.calculate_price() + extra_charge
        return total


print("Enter 1 for GOLD Ticket")
print("Enter 2 for PLATINUM Ticket")
print("Enter 3 for VIP Ticket")

choice = int(input("Enter Your Choice : "))


if choice == 1:
    obj = GoldTicket("Dhurandhar", 2, 1000)
    print("Gold Ticket Booked")
    print("Movie Name :", obj.get_movie_name())
    print("Final Price :", obj.final_price())

elif choice == 2:
    obj = PlatinumTicket("Dhurandhar", 2, 1000)
    print("Platinum Ticket Booked")
    print("Movie Name :", obj.get_movie_name())
    print("Final Price :", obj.final_price())

elif choice == 3:
    obj = VIPTicket("Dhurandhar", 2, 1000)
    print("VIP Ticket Booked")
    print("Movie Name :", obj.get_movie_name())
    print("Final Price :", obj.final_price())

else:
    print("Invalid Choice")