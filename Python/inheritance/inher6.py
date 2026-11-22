# 6. Hospital Management

# Parent:

# HospitalStaff

# Child:

# Doctor
# Nurse
# Receptionist

# Implement duties().

class HospitalStaff():
    def __init__(self, id , name):
        self.__id = id
        self.__name = name

    def get_id(Self):
        return self.__id

    def get_name(self):
        return self.__name

    def duties(self):
        print("hospital duties")

class Doctor(HospitalStaff):
    def duties(self):
        print("to operate patient.")

class Nurse(HospitalStaff):
    def duties(self):
        print("to assisst doctore.")

class Receptionist(HospitalStaff):
    def duties(Self):
        print("to provide details at reception ")

doc = Doctor("101", "Ishika")
nur = Nurse("201", "ganesh")
rec = Receptionist("301", "siaa")

print(doc.get_name())
doc.duties()

print(nur.get_name())
nur.duties()

print(rec.get_name())
rec.duties()
