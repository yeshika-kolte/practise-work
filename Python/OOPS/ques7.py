# 7. Hospital Patient Record System
# Problem

# Create a patient management system.

# Requirements

# Each patient should contain:

# patient id
# name
# disease
# doctor assigned
# Functionalities
# Display patient details
# Change doctor
# Count total patients admitted
# Additional Task

# Create patient from formatted string using class method.

class patient:
    total_patients = 0
    
    def __init__(self, patient_id, name, disease, doctor_assigned):
        self.patient_id = patient_id
        self.name = name
        self.disease = disease
        self.doctor_assigned = doctor_assigned
        patient.total_patients += 1

    def display_details(self):
        print(f"Patient ID: {self.patient_id}, Name: {self.name}, "
              f"Disease: {self.disease}, Doctor Assigned: {self.doctor_assigned}")

    def change_doctor(self, new_doctor):
        self.doctor_assigned = new_doctor

    @classmethod
    def from_string(cls, patient_str):
        patient_id, name, disease, doctor_assigned = patient_str.split("-")
        return cls(patient_id, name, disease, doctor_assigned)

p1 = patient.from_string("001-RAM SINGH-FLU-Dr.ANSH KOLTE")
p1.display_details()
p1.change_doctor("Dr.ANSH KOLTE")
p1.display_details()
print("Total Patients Admitted:", patient.total_patients)