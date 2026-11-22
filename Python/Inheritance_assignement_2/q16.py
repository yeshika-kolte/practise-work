from abc import ABC, abstractmethod

class Patient(ABC):
    @abstractmethod
    def hospital_bill(self):
        pass

class GeneralPatient(Patient):
    def hospital_bill(self):
        print("General Patient Bill : 5000")

class ICUPatient(Patient):
    def hospital_bill(self):
        print("ICU Patient Bill : 20000")

class EmergencyPatient(Patient):
    def hospital_bill(self):
        print("Emergency Patient Bill : 10000")

obj1 = GeneralPatient()
obj1.hospital_bill()

obj2 = ICUPatient()
obj2.hospital_bill()

obj3 = EmergencyPatient()
obj3.hospital_bill()