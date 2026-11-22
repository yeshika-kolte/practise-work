'''18. Vehicle Insurance System
Vehicle
InsuredVehicle
Car

Calculate insurance amount.'''

class Vehicle:
    def __init__(self,vehicle_type,fuel_type):
        self.__vehicle_type = vehicle_type
        self.__fuel_type = fuel_type

    def get_vehicleName(self):
        return self.__vehicle_type
    
    def get_fuelType(self):
        return self.__fuel_type
    
class InsuredVehicle(Vehicle):
    def __init__(self, vehicle_type, fuel_type,status,amount):
        super().__init__(vehicle_type, fuel_type)
        self.__status = status
        self.__amount = amount

    def get_status(self):
        return self.__status
    
    def get_insurance_amount(self):
        return self.__amount
    
class Car(InsuredVehicle):
    def __init__(self, vehicle_type, fuel_type, status, amount,model):
        super().__init__(vehicle_type, fuel_type, status, amount)
        self.__model = model

    def detail(self):
        print(f"Vehicle Type :{self.get_vehicleName()}")
        print(f"Model : {self.__model}")
        print(f"Fuel Type : {self.get_fuelType()}")
        print(f"Insurance Status : {self.get_status()}")
        print(f"Insurance Amount : {self.get_insurance_amount()}")
    

car = Car("Car","Petrol",True,10000,"BMW")

car.detail()