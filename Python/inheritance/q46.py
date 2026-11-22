class Room:
    def __init__(self, room_type, price):
        self.__room_type = room_type
        self.__price = price

    def get_room_type(self):
        return self.__room_type

    def get_price(self):
        return self.__price

class Booking:
    def __init__(self, room, days):
        self.__room = room
        self.__days = days

    def total_price(self):
        return self.__room.get_price() * self.__days

    def booking_details(self):
        print(f"Room Type : {self.__room.get_room_type()}")
        print(f"Days : {self.__days}")
        print(f"Total Price : {self.total_price()}")

obj1 = Room("super-delux", 3000)
obj2 = Booking(obj1, 3)
obj2.booking_details()