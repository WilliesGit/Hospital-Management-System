# Imports
import os
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

#from GUI import root

# Initialising the actors
admin = Admin('admin','123') # username is 'admin', password is '123'
doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
initialized_patients = [Patient('Sara','Smith', 20, '07012345678','B1 234',['Fever' , 'Cold']), Patient('Mike','Jones', 37,'07555551234','L2 2AB',['Headache' , 'Itchiness']), Patient('David','Smith', 15, '07123456789','C1 ABC', ['Rash' , 'Diarrhea'])]


patients = []
discharged_patients = []

admin.doctors = doctors
admin.patients = patients
admin.discharged_patients = discharged_patients


if not os.path.exists('patients_list.csv'):  # Check if the file exists
    admin.save_patients_to_file(initialized_patients)  # Save initialized patients to the file

# Load patients from file and merge with initialized patients (avoid duplicates)
admin.load_patients_from_file(patients, doctors)

existing_patient_names = {p.full_name() for p in patients if isinstance(p, Patient)}

# Add non-duplicate initialized patients
for patient in initialized_patients:
    if patient.full_name() not in existing_patient_names and isinstance(patient, Patient):
        patients.append(patient)


# Save the updated patient list back to the file
admin.save_patients_to_file(patients)


 

