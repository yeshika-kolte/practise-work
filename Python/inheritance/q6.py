'''6. Hospital Management

Parent:

HospitalStaff

Child:

Doctor
Nurse
Receptionist

Implement duties().
'''

from abc import *

class HospitalStaff(ABC):
    @abstractmethod
    def duties(self):
        pass

class Doctor(HospitalStaff):
    def duties(self):
        print("Doctor Duties")


class Nurse(HospitalStaff):
    def duties(self):
        print("Nurse Duties")

class ReceptionList(HospitalStaff):
    def duties(self):
        print("Receptionist Duties")


doctor = Doctor()
doctor.duties()

nurse = Nurse()
nurse.duties()

recList= ReceptionList()
recList.duties()
