from abc import ABC, abstractmethod

class NavigationSystem(ABC):
    @abstractmethod
    def navigate(self):
        pass

class GoogleMaps(NavigationSystem):
    def navigate(self):
        print("Google Maps")

class AppleMaps(NavigationSystem):
    def navigate(self):
        print("Apple Maps")

obj1 = GoogleMaps()
obj1.navigate()
obj2 = AppleMaps()
obj2.navigate()