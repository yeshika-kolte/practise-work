from abc import ABC, abstractmethod

class Passenger:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

class Train:
    def __init__(self, train_name, seats):
        self.__train_name = train_name
        self.__seats = seats

    def get_train_name(self):
        return self.__train_name

    def get_seats(self):
        return self.__seats

    def set_seats(self, seats):
        self.__seats = seats

class Ticket(ABC):

    @abstractmethod
    def booking(self):
        pass

class RailwayTicket(Ticket):
    def __init__(self, passenger, train):
        self.__passenger = passenger
        self.__train = train

    def booking(self):
        if self.__train.get_seats() > 0:
            remaining = self.__train.get_seats() - 1
            self.__train.set_seats(remaining)
            print(f"Name : {self.__passenger.get_name()}")
            print(f"Train : {self.__train.get_train_name()}")
            print(f"Remaining Seats : {self.__train.get_seats()}")
        else:
            print("No Seats")

p1 = Passenger("Rahul")
t1 = Train("Vande Bharat", 2)
obj1 = RailwayTicket(p1, t1)
obj1.booking()