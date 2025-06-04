from Doctor import Doctor
from Patient import Patient



class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
       


    def login(self, username: str, password: str) -> bool:
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
        
        if self.__username in username and self.__password == password:
            return True
        
        else:
            return False

   

       
    def get_doctors(self):
        
        return self.doctors
    
    def get_doctor_details(self, doctors, first_name, surname, speciality) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        
        if not first_name or not surname or not speciality:
            print("Invalid input: all fields are required.")
            return False
        
       
        for doctor in doctors:
            if first_name == doctor.get_first_name() and surname == doctor.get_surname():
             
                print('Doctor with this name already exists.')
                return False # or you could return an error message
    
        
        doctor = Doctor(first_name, surname, speciality)
        doctors.append(doctor)
        
        return True
    
    def update_doctor_details(self, doctor_id, new_first_name=None, new_surname=None, new_speciality=None):
        try:
            # Convert the doctor_id to a n index (0-based)
            doctor_index = int(doctor_id) - 1

            # Check if doctor_id is valid
            if doctor_index < 0 or doctor_index >= len(self.doctors):
                return False, "Invalid Doctor ID. No doctor found with this ID."

            doctor = self.doctors[doctor_index]

            # Update fields only if new values are provided
            if new_first_name:
                doctor.set_first_name(new_first_name.strip())
            if new_surname:
                doctor.set_surname(new_surname.strip())
            if new_speciality:
                doctor.set_speciality(new_speciality.strip())

            return True, f"Doctor ID {doctor_id} updated successfully."
        except ValueError:
            return False, "Doctor ID must be a valid number."
        except Exception as e:
            return False, f"An error occurred: {str(e)}"
        
        
    def delete_doctor(self, doctor_id):
        try:
            # Convert the doctor_id to an index (0-based)
            doctor_index = int(doctor_id) - 1

            # Check if doctor_id is valid
            if doctor_index < 0 or doctor_index >= len(self.doctors):
                return False, "Invalid Doctor ID. No doctor found with this ID."

            removed_doctor = self.doctors.pop(doctor_index)
            

            return True, f"Doctor ID {doctor_id} deleted successfully."
        except ValueError:
            return False, "Doctor ID must be a valid number."
        except Exception as e:
            return False, f"An error occurred: {str(e)}"
        
    def get_patients(self):
        
        enriched_patients = []
        for patient in self.patients:
            enriched_patients.append({
                'full_name': patient.full_name(),
                'doctor_name': patient.get_doctor(),
                'age': patient.get_age(),
                'mobile': patient.get_mobile(),
                'post_code': patient.get_postcode(),
                'symptoms': ', '.join(patient.get_symptoms())
            })
        return enriched_patients

   
    
        
    def get_patient_details(self, patients, first_name, surname, age, mobile, postcode, symptoms, doctors, doctor_id):
        """
        Registers a new patient and assigns them to a doctor.
        """
       
    
        # Check if the patient already exists
        for patient in patients:
            if first_name == patient.get_first_name() and surname == patient.get_surname():
                return False, f"A patient with the name {first_name} {surname} already exists."
    
        # Create new patient object
        patient = Patient(first_name, surname, age, mobile, postcode, symptoms)
    
        # Validate doctor ID
        try:
            doctor_index = int(doctor_id) - 1
            if doctor_index < 0 or doctor_index >= len(doctors):
                return False, f"Invalid Doctor ID: {doctor_id}. Please select a valid ID."
        except ValueError:
            return False, "Doctor ID must be a valid integer."
    
        # Assign patient to doctor
        doctor = doctors[doctor_index]
        patient.link(doctor)
        doctor.add_patient(patient)
        print(f"Patient {first_name} {surname} has been assigned to Dr. {doctor.full_name()}.")
    
        # Add the patient to the list
        patients.append(patient)
    
        # Save to file
        self.save_patients_to_file(patients)
    
        print("Patient registration successful!")
        return True, (first_name, surname, age, mobile, postcode, symptoms)


    def update_patient_detail(self, patients, patient_id, doctors, doctor_id=None, new_first_name=None, new_surname=None, new_age=None, new_mobile=None, new_postcode=None, new_symptoms=None):
        try:
            # Convert the patient_id to an index (0-based)
            patient_index = int(patient_id) - 1

            # Check if patient_id is valid
            if patient_index < 0 or patient_index >= len(self.patients):
                return False, "Invalid Patient ID. No Patient found with this ID."

            patient = self.patients[patient_index]
            
            

            # Update fields only if new values are provided
            if new_first_name:
                patient.set_first_name(new_first_name)
            if new_surname:
                patient.set_surname(new_surname)
            if new_age:
                patient.set_age(new_age)
            if new_mobile:
                patient.set_mobile(new_mobile)
            if new_postcode:
                patient.set_postcode(new_postcode)
            if new_symptoms:
                patient.set_symptoms(new_symptoms)
                
                # Get the current doctor of the patient
            current_doctor = patient.get_doctor()
    
            if doctor_id:
                try:
                    print(f"Doctor ID received: '{doctor_id}'")  # Debugging output
                    # Convert doctor_id to an index (0-based)
                    doctor_index = int(doctor_id) - 1
    
                    # Check if doctor_id is valid
                    if doctor_index < 0 or doctor_index >= len(doctors):
                        return False, f"Invalid Doctor ID: {doctor_id}. Please select a valid ID."
    
                    # Get the new doctor object
                    new_doctor = doctors[doctor_index]
    
                    # Check if the patient is already assigned to this doctor
                    if current_doctor == new_doctor.full_name():
                        return False, "The patient is already assigned to this doctor."

                    # Assign the new doctor
                    patient.link(new_doctor)
                    new_doctor.add_patient(patient)
                    print(f"Patient {patient.get_first_name()} {patient.get_surname()} has been reassigned to Dr. {new_doctor.full_name()}.")
                except ValueError:
                    return False, "Doctor ID must be a valid integer."
            else:
                # Unassign the current doctor if no doctor_id is provided
                if current_doctor:
                    current_doctor.remove_patient(patient)
                    patient.set_doctor(None)
                    print(f"Patient {patient.get_first_name()} {patient.get_surname()} has been unassigned from any doctor.")

            
            #Saves the updated list back to the file
            self.save_patients_to_file(patients)
                
            return True, f"Patient ID {patient_id} updated successfully."
        except ValueError:
            return False, "Patient ID must be a valid number."
        except Exception as e:
            return False, f"An error occurred: {str(e)}"
        
        
        
    def delete_patient(self, patient_id):
        try:
            # Convert the patient_id to an index (0-based)
            patient_index = int(patient_id) - 1

            # Check if doctor_id is valid
            if patient_index < 0 or patient_index >= len(self.patients):
                return False, "Invalid Paitnet ID. No Patient found with this ID."
            
            # Remove the patient from the list
            removed_patient = self.patients.pop(patient_index)
            self.save_patients_to_file(self.patients)

            return True, f"Patient ID {patient_id} deleted successfully."
        except ValueError:
            return False, "Patient ID must be a valid number."
        except Exception as e:
            return False, f"An error occurred: {str(e)}"
    
    
    def save_patients_to_file(self, patients):
        """
        patients :Saves patients to a file
        """
        try:
            with open("patients_list.csv", "w") as patients_file:
                for patient in patients:
                    doctor_name = patient.get_doctor()
                    symptoms_str = "|".join(patient.get_symptoms())
                    patients_file.write(
                        f"{patient.get_first_name()},{patient.get_surname()},{patient.get_age()},{patient.get_mobile()},{patient.get_postcode()},{symptoms_str},{doctor_name}\n")
            
            return True  # Successfully saved the data
        except Exception as e:
            print("Error saving patient data: ", e)
            
            
    def load_patients_from_file(self, patients, doctors):
        """ Loads patients data from a file """
        try:
            # Clear the existing patient list to ensure fresh load
            self.patients.clear()
    
            # Try to open and read the file
            with open("patients_list.csv", "r") as patients_file:
                for line in patients_file:
                    # Split line into parts (with a maximum of 7 parts to match columns)
                    parts = line.strip().split(",", 6)
                    if len(parts) == 7:
                        first_name, surname, age, mobile, postcode, symptoms, doctor_name = parts
                        symptoms = symptoms.split("|")  # Split symptoms by "|"
                        
                        # Ensure valid age conversion and handle invalid data gracefully
                        try:
                            age = int(age)
                        except ValueError:
                            print(f"Invalid age '{age}' for patient {first_name} {surname}, skipping.")
                            continue  # Skip the invalid line
                        
                        # Create the Patient object
                        patient = Patient(first_name, surname, age, mobile, postcode, symptoms)
                        
                        doctor = None 
                        
                        # Try to find the doctor based on the doctor's full name
                        for doc in doctors:
                            if doc.full_name() == doctor_name:
                                doctor = doc
                                patient.set_doctor(doctor)
                                break
                        # If doctor is found, assign to the patient
                        if doctor is None:
                            print(f"Doctor {doctor_name} not found for patient {first_name} {surname}. Assigning None.")
    
                        # Append the patient object to the list
                        self.patients.append(patient)
    
            return True  # Successfully loaded the data
    
        except FileNotFoundError:
            print("File not found: Initializing new patient data.")
            return False  # File not found
    
        except Exception as e:
            print(f"Error loading patient data: {e}")
            return False  # For any other errors

  
    
    
    def grouped__patients_by_surname(self,patients):
        """Group patients by surname."""
        grouped_patients = {}
        for patient in patients:
            surname = patient['full_name'].split()[-1]  # Extract surname
            if surname not in grouped_patients:
                grouped_patients[surname] = []
            grouped_patients[surname].append(patient)
        return grouped_patients
    
    

   

    def assign_doctor_to_patient(self, patients, patient_id, doctors, doctor_id=None):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        try:
            # Convert the patient_id to an index (0-based)
            patient_index = int(patient_id) - 1

            # Check if patient_id is valid
            if patient_index < 0 or patient_index >= len(self.patients):
                return False, "Invalid Patient ID. No Patient found with this ID."

            patient = self.patients[patient_index]
                
                # Get the current doctor of the patient
            current_doctor = patient.get_doctor()
            print(f"{current_doctor}")
    
            if doctor_id:
                try:
                    print(f"Doctor ID received: {doctor_id} ")  # Debugging output
                    # Convert doctor_id to an index (0-based)
                    doctor_index = int(doctor_id) - 1
    
                    # Check if doctor_id is valid
                    if doctor_index < 0 or doctor_index >= len(doctors):
                        return False, f"Invalid Doctor ID: {doctor_id}. Please select a valid ID."
    
                    # Get the new doctor object
                    new_doctor = doctors[doctor_index]
    
                    # Check if the patient is already assigned to this doctor
                    if current_doctor == new_doctor.full_name():
                        return False, "The patient is already assigned to this doctor."
    
                    # Assign the new doctor
                    patient.link(new_doctor)
                    new_doctor.add_patient(patient)
                    print(f"Patient {patient.get_first_name()} {patient.get_surname()} has been assigned to Dr. {new_doctor.full_name()}.")
                except ValueError:
                    return False, "Doctor ID must be a valid integer."
            else:
                # Unassign the current doctor if no doctor_id is provided
                if current_doctor:
                    current_doctor.remove_patient(patient)
                    patient.set_doctor(None)
                    print(f"Patient {patient.get_first_name()} {patient.get_surname()} has been unassigned from any doctor.")

            
            #Saves the updated list back to the file
            self.save_patients_to_file(patients)
                
            return True, f"Patient ID {patient_id} assigned successfully."
        except ValueError:
            return False, "Patient ID must be a valid number."
        except Exception as e:
            return False, f"An error occurred: {str(e)}"
       
  
            
    def relocate_doctor_to_patient(self, patients, patient_id, doctors, doctor_id=None):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        try:
            # Convert the patient_id to an index (0-based)
            patient_index = int(patient_id) - 1

            # Check if patient_id is valid
            if patient_index < 0 or patient_index >= len(self.patients):
                return False, "Invalid Patient ID. No Patient found with this ID."

            patient = self.patients[patient_index]
                
                # Get the current doctor of the patient
            current_doctor = patient.get_doctor()
            print(f"{current_doctor}")
    
            if doctor_id:
                try:
                    print(f"Doctor ID received: {doctor_id} ")  # Debugging output
                    # Convert doctor_id to an index (0-based)
                    doctor_index = int(doctor_id) - 1
    
                    # Check if doctor_id is valid
                    if doctor_index < 0 or doctor_index >= len(doctors):
                        return False, f"Invalid Doctor ID: {doctor_id}. Please select a valid ID."
    
                    # Get the new doctor object
                    new_doctor = doctors[doctor_index]
    
                    # Check if the patient is already assigned to this doctor
                    if current_doctor == new_doctor.full_name():
                        return False, "The patient is already assigned to this doctor."
                    

                        
                    if current_doctor and new_doctor != None:
                        # Assign the new doctor
                        patient.link(new_doctor)
                        new_doctor.add_patient(patient)
                        print(f"Patient {patient.get_first_name()} {patient.get_surname()} has been reassigned to Dr. {new_doctor.full_name()}.")
                    else:
                        return False, "You cannot reassign patient's Doctor with previously 'None' Doctor"
                        
                except ValueError:
                    return False, "Doctor ID must be a valid integer."
            else:
                # Unassign the current doctor if no doctor_id is provided
                if current_doctor:
                    current_doctor.remove_patient(patient)
                    patient.set_doctor(None)
                    print(f"Patient {patient.get_first_name()} {patient.get_surname()} has been unassigned from any doctor.")

            
            #Saves the updated list back to the file
            self.save_patients_to_file(patients)
                
            return True, f"Patient ID {patient_id} reassigned successfully."
        except ValueError:
            return False, "Patient ID must be a valid number."
        except Exception as e:
            return False, f"An error occurred: {str(e)}"
        
            
        
            
    def create_appointment(self, patients, patient_id, date, time, notes, doctors, doctor_id=None):
        """
        Create and assign an appointment for a patient with a doctor.
        Args:
            doctors (list<Doctor>): List of all doctors.
            patients (list<Patient>): List of all patients.
        """
        
        try:
            # Convert the patient_id to an index (0-based)
            patient_index = int(patient_id) - 1

            # Check if patient_id is valid
            if patient_index < 0 or patient_index >= len(self.patients):
                return False, "Invalid Patient ID. No Patient found with this ID."

            patient = self.patients[patient_index]
            
                
                # Get the current doctor of the patient
            current_doctor = patient.get_doctor()
    
            if doctor_id:
                try:
                    print(f"Doctor ID received: '{doctor_id}'")  # Debugging output
                    # Convert doctor_id to an index (0-based)
                    doctor_index = int(doctor_id) - 1
    
                    # Check if doctor_id is valid
                    if doctor_index < 0 or doctor_index >= len(doctors):
                        return False, f"Invalid Doctor ID: {doctor_id}. Please select a valid ID."
    
                    # Get the new doctor object
                    new_doctor = doctors[doctor_index]
                    
                                    
                            # Validate date, time, and notes
                    if not date or not time or not notes:
                        return False, "Date, time, and notes are required to schedule an appointment."
        
                    # Create and assign the appointment
                    appointment = {
                        'patient': patient,
                        'date': date,
                        'time': time,
                        'notes': notes,
                    }
                    new_doctor.add_appointment(appointment)
                    return True, f"Appointment scheduled for {patient.full_name()} with {new_doctor.full_name()} on {date} at {time}."
                    print(f"Appointment scheduled for {patient.full_name()} with {new_doctor.full_name()} on {date} at {time}.")
                            
                except ValueError:
                    return False, "Doctor ID must be a valid integer."
            else:
                # Unassign the current doctor if no doctor_id is provided
                if current_doctor:
                    current_doctor.remove_patient(patient)
                    patient.set_doctor(None)
                    print(f"Patient {patient.get_first_name()} {patient.get_surname()} has been unassigned from any doctor.")

            
            #Saves the updated list back to the file
            self.save_patients_to_file(patients)
                
            return True, f"Patient ID {patient_id} updated successfully."
        except ValueError:
            return False, "Patient ID must be a valid number."
        except Exception as e:
            return False, f"An error occurred: {str(e)}"
        
        
    def view_all_appointments(self, doctors):
        """
        Retrieve and compile a list of all appointments across all doctors
        """
        all_appointments = []
    
        for doctor in doctors:
            # Get appointments for the current doctor
            appointments = doctor.get_appointments()
            
            # Append doctor-specific information to each appointment
            for appointment in appointments:
                appointment_details = {
                    "doctor": doctor.full_name(),
                    "patient": appointment['patient'].full_name(),
                    "date": appointment['date'],
                    "time": appointment['time'],
                    "notes": appointment['notes'],
                }
                all_appointments.append(appointment_details)
        
        return all_appointments

        
    def remove_appointment(self, doctors, doctor_name, date, time):
        """
        Remove an appointment from a doctor's schedule based on doctor's name, date, and time.
        """
        try:
            # Locate the doctor by name
            doctor = next((doc for doc in doctors if doc.full_name() == doctor_name), None)
            if not doctor:
                return False, f"Doctor '{doctor_name}' not found."
    
            # Locate the appointment to remove
            appointment_to_remove = next(
                (appt for appt in doctor.get_appointments() if appt["date"] == date and appt["time"] == time),
                None
            )
            if not appointment_to_remove:
                return False, f"No appointment found for doctor '{doctor_name}' on {date} at {time}."
    
            # Remove the appointment
            doctor.remove_appointment(appointment_to_remove)
            return True, f"Appointment successfully removed for doctor '{doctor_name}' on {date} at {time}."
        
        except Exception as e:
            return False, f"An error occurred while removing the appointment: {str(e)}"
  
          

       
    def discharged(self, patient_id, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        """
        
        try:
            patient_index = int(patient_id) - 1
            
            # Check if doctor_id is valid
            if patient_index < 0 or patient_index >= len(self.patients):
                return False, "Invalid Paitnet ID. No Patient found with this ID."
            
          # Remove the patient from the active patients list and add to discharged list
            removed_patient = self.patients.pop(patient_index)
            discharge_patients.append(removed_patient)
                
            try:
                self.save_patients_to_file(self.patients)
                
                return True, f"Patient ID {patient_id} discharged successfully."
                print(f"{removed_patient.full_name()} is discharged")
            except Exception as e:
                print("Error occured: ", e)
                #Saves patients back to the list in the case file update fails
                self.patients.insert(patient_index, removed_patient)

        except Exception as e:
            # Handle unexpected errors
            return False, f"An unexpected error occurred: {str(e)}"
 

    
    # Function to calculate the number of patients by illness type
    def get_patients_by_illness(self,patients):
        """
        Returns a dictionary with illness types as keys and patient counts as values.
        Args:
            patients (list): List of patient objects.
        """
        illness_count = {}
        for patient in patients:
            for illness in patient.get_symptoms():
                print(illness)
                illness_count[illness] = illness_count.get(illness, 0) + 1
        return illness_count
    
        
        

    def update_details(self, new_username, new_password, confirm_password):
        """
        Allows the user to update and change username, password and address
        """
        self.__username = new_username

        if new_password == confirm_password:
            self.__password = new_password
            return True, "Admin details updated successfully!"
        else:
            return False, "Passwords do not match. Please try again."
