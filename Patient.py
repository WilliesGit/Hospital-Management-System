from Person import Person

class Patient(Person):
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode, symptoms):
        super().__init__(first_name, surname)
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """   
        self.__doctor = None
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__symptoms = symptoms if isinstance(symptoms, list) else [symptoms]
       
    def get_age(self) :
        return self.__age

    def set_age(self, new_age):
        self.__age = new_age
    
    def get_mobile(self) :
        return self.__mobile

    def set_mobile(self, new_mobile):
        self.__mobile = new_mobile
        
    def get_postcode(self) :
        return self.__postcode

    def set_postcode(self, new_postcode):
        self.__postcode = new_postcode
    
    def get_doctor(self) :
        return None if not self.__doctor else self.__doctor.full_name()
        
    
    def set_doctor(self, doctor):
        self.__doctor = doctor

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor
    
   
    def add_symptoms(self, symptoms):
        
        if isinstance(symptoms, list):
            self.__symptoms.extend(symptoms)
        else:
            self.__symptoms.append(symptoms)
        
    def get_symptoms(self):
        return self.__symptoms

    def print_symptoms(self):
        """prints all the symptoms"""
        return print(f"{self.__symptoms}")
        
        
    def set_symptoms(self, new_symptoms):
        self.__symptoms = new_symptoms if isinstance(new_symptoms, list) else [new_symptoms]
     

