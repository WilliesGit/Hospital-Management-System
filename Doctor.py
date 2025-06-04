from Person import Person
class Doctor(Person):
    """A class that deals with the Doctor operations"""

    def __init__(self, first_name, surname, speciality):
        super().__init__(first_name, surname)
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            speciality (string): Doctor`s speciality
        """

        
        self.__speciality = speciality
        self.__patients = []
        self.__appointments = []

   

    def get_speciality(self) :
        return self.__speciality
    

    def set_speciality(self, new_speciality):
        self.__speciality = new_speciality


    def add_patient(self, patient):
        if patient not in self.__patients:
           self.__patients.append(patient)

          
    def remove_patient(self, patient):
       if patient in self.patients:
           self.__patients.remove(patient)

        
    def get_patients(self):
        return self.__patients

    def add_appointment(self, appointment):
        """
        Adds an appointment to the doctor.
        """
        self.__appointments.append(appointment)

    def remove_appointment(self, appointment):
        """
        Removes an appointment from the doctor.
        """
        if appointment in self.__appointments:
            self.__appointments.remove(appointment)

    def get_appointments(self):
        return self.__appointments
   


    def __str__(self) :
        return f'{self.full_name():^30}|{self.__speciality:^15}'
