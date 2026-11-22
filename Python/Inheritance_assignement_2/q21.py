from abc import ABC, abstractmethod

class Subscription(ABC):
    @abstractmethod
    def plan_details(self):
        pass

class BasicPlan(Subscription):
    def plan_details(self):
        print("Basic Plan")
        print("Price : 199")
        print("Screen Limit : 1")

class StandardPlan(Subscription):
    def plan_details(self):
        print("Standard Plan")
        print("Price : 499")
        print("Screen Limit : 2")

class PremiumPlan(Subscription):
    def plan_details(self):
        print("Premium Plan")
        print("Price : 999")
        print("Screen Limit : 4")

obj1 = BasicPlan()
obj1.plan_details()
# obj2 = StandardPlan()
# obj2.plan_details()
# obj3 = PremiumPlan()
# obj3.plan_details()