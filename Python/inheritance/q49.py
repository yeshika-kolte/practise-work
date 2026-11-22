from abc import ABC, abstractmethod

class Movie:
    def __init__(self, movie_name):
        self.__movie_name = movie_name

    def get_movie_name(self):
        return self.__movie_name


class Subscription(ABC):
    @abstractmethod
    def plan_details(self):
        pass

class BasicPlan(Subscription):
    def plan_details(self):
        print("Basic Plan : 399/month")

class PremiumPlan(Subscription):
    def plan_details(self):
        print("Premium Plan : 999/month")

class WatchHistory:
    def __init__(self, movie):
        self.__movie = movie

    def display_history(self):
        print(f"Recently Watched : {self.__movie.get_movie_name()}")


obj1 = Movie("romio juilet")
obj2 = BasicPlan()
obj3 = WatchHistory(obj1)

obj2.plan_details()
obj3.display_history()