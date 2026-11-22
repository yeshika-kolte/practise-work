from abc import ABC, abstractmethod

class CabBooking(ABC):
    def __init__(self, user, distance, driver):
        self.__user = user
        self.__distance = distance
        self.__driver = driver

    def get_user(self):
        return self.__user
    
    def get_distance(self):
        return self.__distance
    
    def get_driver(self):
        return self.__driver

    @abstractmethod
    def fare_calculation(self):
        pass

    @abstractmethod
    def driver_assignment(self):
        pass

class Cab(CabBooking):
    def fare_calculation(self):
        fare = self.get_distance() * 10
        print(f"User : {self.get_user()}")
        print(f"Cab Fare : {fare}")

    def driver_assignment(self):
        print(f"Driver : {self.get_driver()}")

obj1 = Cab("riaa", 12 , "Rohan")
obj1.driver_assignment()
obj1.fare_calculation()