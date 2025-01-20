from clinic.dao.patient_dao import PatientDAO
from clinic.patient import *
from clinic.exception.invalid_login_exception import InvalidLoginException
from clinic.exception.duplicate_login_exception import DuplicateLoginException
from clinic.exception.invalid_logout_exception import InvalidLogoutException
from clinic.exception.illegal_access_exception import IllegalAccessException
from clinic.exception.illegal_operation_exception import IllegalOperationException
from clinic.exception.no_current_patient_exception import NoCurrentPatientException
import json
from clinic.dao.patient_decoder import PatientDecoder
from clinic.dao.patient_encoder import PatientEncoder

class PatientDAOJSON():
    
    def __init__ (self, PatientDAO, autosave=False):
        self.autosave = autosave
        self.filename = 'clinic/patients.json'      # where the patient data will be stored
        self.cur_patient = None
        self.patientsdict = {} #key: string phn, value: Patient a patient. stores all created patients based on their phn
        
        if self.autosave:       #if autosave is on then try to load patient data from file
            try:
                with open(self.filename, 'r') as file:
                    self.patientsdict = json.load(file, cls=PatientDecoder)
            except(FileNotFoundError, json.JSONDecodeError):
                self.patientsdict = {} 
        else:
            self.patientsdict = {}

    #creates a new patient with the information provided and stores them in the patient dictionary
    def create_patient(self, patient) -> None:
        if str(patient.get_phn()) in self.patientsdict:
            raise IllegalOperationException #patient with that phn already exists
        self.patientsdict[str(patient.get_phn())] = patient

        if self.autosave:       # if autosave is on then write the patient data into the file
            with open(self.filename, 'w') as file:
                json.dump(self.patientsdict, file, cls=PatientEncoder, indent=4)
        return patient
    
    #Searches the patient dictionary for the given phn and returns the phn if found
    def search_patient(self, search_num: int) -> Patient:
            search_num = str(search_num)
            if search_num in self.patientsdict:
                return self.patientsdict[search_num]
            else:
                return None
        
    #searches all patient names and any that contain the characters string are added to a list which is to be returned
    def retrieve_patients(self, characters: str) -> list:
        retrieved_patients = []
        for patient in self.patientsdict:
            if characters in self.patientsdict[patient].get_name():
                retrieved_patients.append(self.patientsdict[patient])
        return retrieved_patients
        
    #searches for a patient in the patient dictionary and updates their info with new info
    def update_patient(self, search_phn: int, patient) -> bool:
        search_phn = str(search_phn)
        if (str(patient.get_phn()) in self.patientsdict) and (str(patient.get_phn()) != search_phn): #checks if the new phn is that of a different patient
            raise IllegalOperationException
        if search_phn not in self.patientsdict:
            raise IllegalOperationException
        if self.cur_patient != None:
            if search_phn == str(self.cur_patient.get_phn()): # can't change current patient
                raise IllegalOperationException
        self.patientsdict[search_phn].set_phn(patient.get_phn())
        self.patientsdict[search_phn].set_name(patient.get_name())
        self.patientsdict[search_phn].set_birth_date(patient.get_birth_date())
        self.patientsdict[search_phn].set_phone(patient.get_phone())
        self.patientsdict[search_phn].set_email(patient.get_email())
        self.patientsdict[search_phn].set_address(patient.get_address())

        self.patientsdict[str(patient.get_phn())] = self.patientsdict.pop(search_phn)

        if self.autosave:       # if autosave is on then write the patient data into the file
            with open(self.filename, 'w') as file:
                json.dump(self.patientsdict, file, cls=PatientEncoder, indent=4)
        return True
        
    #takes a phn and deletes the patient with that phn from the patient dictionary
    def delete_patient(self, delete_phn: int) -> bool:
        delete_phn = str(delete_phn)
        if delete_phn not in self.patientsdict:
            raise IllegalOperationException
        if self.cur_patient != None:
            if delete_phn == str(self.cur_patient.get_phn()): # can't delete current patient
                raise IllegalOperationException
        self.patientsdict.pop(delete_phn)

        if self.autosave:       # if autosave is on then write the patient data into the file
            with open(self.filename, 'w') as file:
                json.dump(self.patientsdict, file, cls=PatientEncoder, indent=4)
        return True
    
    #returns a list of all patients in the patient dictionary
    def list_patients(self) -> list:
        patient_list = []
        for patient in self.patientsdict:
            patient_list.append(self.patientsdict[patient])
        return patient_list
    
    #sets a patient as the current patient
    def set_current_patient(self, current_phn: int) -> bool:
        if self.is_logged:
            if current_phn not in self.patientsdict:
                raise IllegalOperationException
            self.cur_patient = self.patientsdict[current_phn]
            return True
        else:
            raise IllegalAccessException
        
    #returns the current patient
    def get_current_patient(self) -> Patient:
        if self.is_logged:
            return self.cur_patient
        else:
            raise IllegalAccessException
        
    #unsets the current patient
    def unset_current_patient(self) -> bool:
        if self.is_logged:
            self.cur_patient = None
            return True
        else:
            raise IllegalAccessException