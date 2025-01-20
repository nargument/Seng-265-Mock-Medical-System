from clinic.patient import *
#from clinic.patientrecord import *
from clinic.note import *

class Controller:
    
    def __init__(self) -> None:
        self.username = 'user'
        self.password = 'clinic2024'
        self.is_logged = False
        self.cur_patient = None
        self.patientsdict = {} #key: int phn, value: Patient a patient. stores all created patients based on their phn

    #takes a username and password, checks if they're correct, if yes logs user in and returns true if not returns false
    def login(self, username: str, password: str) -> bool:
        if self.is_logged:
            return False
        if username != self.username:
            return False
        if password != self.password:
            return False
        self.is_logged = True
        return self.is_logged
    
    #if the user is logged in logs them out, returns false if they aren't logged in yet esle returns true 
    def logout(self) -> bool:
        if not self.is_logged:
            return False
        self.is_logged = False
        return True

    #CHANGED: this no longer sets the new patient to the current patient now it creates the new patient as a temp then stores them in the patient dictionary
    #creates a new patient with the information provided and stores them in the patient dictionary
    def create_patient(self, phn: int, name: str, birth_date: str, phone: str, email: str, address: str) -> None:
        if self.is_logged:
            if phn in self.patientsdict:
                return None #patient with that phn already exists
            temp_patient = Patient(phn, name, birth_date, phone, email, address)
            self.patientsdict[temp_patient.get_phn()] = temp_patient
            return temp_patient
        else:
            return None  # Return None if not logged in

    #Searches the patient dictionary for the given phn and returns the phn if found
    def search_patient(self, search_num: int) -> Patient:
        if self.is_logged:
            if search_num in self.patientsdict:
                return self.patientsdict[search_num]
        else:
            return None
        
    #searches all patient names and any that contain the characters string are added to a list which is to be returned
    def retrieve_patients(self, characters: str) -> list:
        retrieved_patients = []
        if self.is_logged:
            for patient in self.patientsdict:
                if characters in self.patientsdict[patient].get_name():
                    retrieved_patients.append(self.patientsdict[patient])
            return retrieved_patients
        else:
            return None
        
    #searches for a patient in the patient dictionary and updates their info with new info
    def update_patient(self, search_phn: int, new_phn: int, new_name: str, new_birth_date: str, new_phone: str, new_email: str, new_address: str) -> bool:
        if self.is_logged:
            if (new_phn in self.patientsdict) and (new_phn != search_phn): #checks if the new phn is that of a different patient
                return None
            if search_phn not in self.patientsdict:
                return None
            if self.cur_patient != None:
                if search_phn == self.cur_patient.get_phn():
                    return False
            self.patientsdict[search_phn].set_phn(new_phn)
            self.patientsdict[search_phn].set_name(new_name)
            self.patientsdict[search_phn].set_birth_date(new_birth_date)
            self.patientsdict[search_phn].set_phone(new_phone)
            self.patientsdict[search_phn].set_email(new_email)
            self.patientsdict[search_phn].set_address(new_address)

            self.patientsdict[new_phn] = self.patientsdict.pop(search_phn)
            return True
        else:
            return None
        
    #takes a phn and deletes the patient with that phn from the patient dictionary
    def delete_patient(self, delete_phn: int) -> bool:
        if self.is_logged:
            if delete_phn not in self.patientsdict:
                return None
            if self.cur_patient != None:
                if delete_phn == self.cur_patient.get_phn():
                    return False
            self.patientsdict.pop(delete_phn)
            return True
        else:
            return None
    
    #returns a list of all patients in the patient dictionary
    def list_patients(self) -> list:
        patient_list = []
        if self.is_logged:
            for patient in self.patientsdict:
                patient_list.append(self.patientsdict[patient])
            return patient_list
        else:
            return None
    
    #sets a patient as the current patient
    def set_current_patient(self, current_phn: int) -> bool:
        if self.is_logged:
            if current_phn not in self.patientsdict:
                return None
            self.cur_patient = self.patientsdict[current_phn]
            return True
        else:
            return None
        
    #returns the current patient
    def get_current_patient(self) -> Patient:
        if self.is_logged:
            return self.cur_patient
        else:
            return None
        
    #unsets the current patient
    def unset_current_patient(self) -> bool:
        if self.is_logged:
            self.cur_patient = None
            return True
        else:
            return None
    
    #creates a note
    def create_note(self, text: str) -> Note:
        if self.is_logged:
            if self.cur_patient:
                return self.cur_patient.create_note(text)
        else:
            return None
    
    #searches note according to code        
    def search_note(self, code: int) -> Note:
        if self.is_logged:
            if self.cur_patient:
                return self.cur_patient.search_note(code)
        else:
            return None
    
    #returns notes that contains a specific string in a list        
    def retrieve_notes(self, text: str) -> list:
        if self.is_logged:
            if self.cur_patient:
                return self.cur_patient.retrieve_notes(text)
        else:
            return None
    
    #updates note according to the code and text given
    def update_note(self, code: int, new_text: str) -> bool:
        if self.is_logged:
            if self.cur_patient:
                return self.cur_patient.update_note(code, new_text)
        else:
            return False
    
    #deletes a note
    def delete_note(self, code: int) -> bool:
        if self.is_logged:
            if self.cur_patient:
                return self.cur_patient.delete_note(code)
        else:
            return False
    #lists all the notes that current patient has
    def list_notes(self) -> list:
        if self.is_logged:
            if self.cur_patient:
                return self.cur_patient.list_notes()
        else:
            return None
