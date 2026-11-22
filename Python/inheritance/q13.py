'''13. Smart Device System
Device
SmartDevice(Device)
SmartTV(SmartDevice)

Add WiFi support.

'''

class Device:
    def __init__(self,name,brand):
        self.__name = name
        self.__brand= brand

    def get_name(self):
        return self.__name
    
    def get_brand(self):
        return self.__brand
    

class SmartDevice(Device):
    def __init__(self, name, brand,type):
        super().__init__(name, brand)
        self.__type = type

    def get_type(self):
        return self.__type
    
    def wifi_support(self):
        return True

    
class SmartTV(SmartDevice):
    def __init__(self,name,brand,type,screen_size):
        super().__init__(name,brand,type)
        self.__screen_size = screen_size

    def display(self):
        print("-----------Details of Smart TV----------")
        print(f"Model Name : {self.get_name()}")
        print(f"Brand : {self.get_brand()}")
        print(f"Type : {self.get_type()}")
        print(f"Wifi-Support : {self.wifi_support()}")
        print(f"Screen Size : {self.__screen_size}")


tv1 = SmartTV(" Sony BRAVIA 3 ","Sony","Google TV",43)

tv1.display()