import hashlib
from clinic.patient import *
from clinic.note import *
from clinic.exception.invalid_login_exception import InvalidLoginException
from clinic.exception.duplicate_login_exception import DuplicateLoginException
from clinic.exception.invalid_logout_exception import InvalidLogoutException
from clinic.exception.illegal_access_exception import IllegalAccessException
from clinic.exception.illegal_operation_exception import IllegalOperationException
from clinic.exception.no_current_patient_exception import NoCurrentPatientException
from clinic.dao.patient_dao_json import *
from clinic.dao.patient_dao import *
class Controller:
    
    def __init__(self, autosave) -> None:
        self.autosave = autosave
        self.is_logged = False
        #self.cur_patient = None
        self.filename = 'clinic/users.txt'
        self.users = self.load_users()
        self.patient_dao = PatientDAOJSON(PatientDAO, self.autosave)

    # load users from the file
    def load_users(self):
        users = {}
        with open(self.filename, 'r') as file:
            for line in file:
                line_list = line.split(',')
                users[line_list[0]] = line_list[1].strip()
        return users
    
    # 
    def get_password_hash(self, password):
        encoded_password = password.encode('utf-8')     # Convert the password to bytes
        hash_object = hashlib.sha256(encoded_password)      # Choose a hashing algorithm (e.g., SHA-256)
        hex_dig = hash_object.hexdigest()       # Get the hexadecimal digest of the hashed password
        return hex_dig

    #takes a username and password, checks if they're correct, if yes logs user in and returns true if not returns false
    def login(self, username: str, password: str) -> bool:
        if self.is_logged:
            raise DuplicateLoginException
        if self.users.get(username):
            password_hash = self.get_password_hash(password)
            if self.users.get(username) == password_hash:
                self.is_logged = True
                return self.is_logged
            else:
                raise InvalidLoginException
        else:
            raise InvalidLoginException
    
    #if the user is logged in logs them out, returns false if they aren't logged in yet esle returns true 
    def logout(self):
        if not self.is_logged:
            raise InvalidLogoutException
        else: 
            self.is_logged = False
            return True

    #creates a new patient with the information provided and stores them in the patient dictionary
    def create_patient(self, phn: int, name: str, birth_date: str, phone: str, email: str, address: str) -> None:
        patient = Patient(phn, name, birth_date, phone, email, address)
        if self.is_logged:
            return self.patient_dao.create_patient(patient)
        else:
            raise IllegalAccessException

    #Searches the patient dictionary for the given phn and returns the phn if found
    def search_patient(self, search_num: int) -> Patient:
        if self.is_logged:
            return self.patient_dao.search_patient(search_num)
        else:
            raise IllegalAccessException
        
    #searches all patient names and any that contain the characters string are added to a list which is to be returned
    def retrieve_patients(self, characters: str) -> list:
        if self.is_logged:
            return self.patient_dao.retrieve_patients(characters)
        else:
            raise IllegalAccessException
        
    #searches for a patient in the patient dictionary and updates their info with new info
    def update_patient(self, search_phn: int, new_phn: int, new_name: str, new_birth_date: str, new_phone: str, new_email: str, new_address: str) -> bool:
        patient = Patient(new_phn, new_name, new_birth_date, new_phone, new_email, new_address)
        if self.is_logged:
            return self.patient_dao.update_patient(search_phn, patient)
        else:
            raise IllegalAccessException
        
    #takes a phn and deletes the patient with that phn from the patient dictionary
    def delete_patient(self, delete_phn: int) -> bool:
        if self.is_logged:
            return self.patient_dao.delete_patient(delete_phn)
        else:
            raise IllegalAccessException
    
    #returns a list of all patients in the patient dictionary
    def list_patients(self) -> list:
        if self.is_logged:
            return self.patient_dao.list_patients()
        else:
            raise IllegalAccessException
    
    #sets a patient as the current patient
    def set_current_patient(self, current_phn: int) -> bool:
        if self.is_logged:
            if self.search_patient(current_phn) == None:
                raise IllegalOperationException
            #self.cur_patient = self.search_patient(current_phn)
            self.patient_dao.cur_patient = self.search_patient(current_phn)
            return True
        else:
            raise IllegalAccessException
        
    #returns the current patient
    def get_current_patient(self) -> Patient:
        if self.is_logged:
            return self.patient_dao.cur_patient
        else:
            raise IllegalAccessException
        
    #unsets the current patient
    def unset_current_patient(self) -> bool:
        if self.is_logged:
            self.patient_dao.cur_patient = None
            return True
        else:
            raise IllegalAccessException
    
    #creates a note
    def create_note(self, text: str) -> Note:
        if self.is_logged:
            if self.patient_dao.cur_patient:
                return self.patient_dao.cur_patient.create_note(text)
            else:
                raise NoCurrentPatientException
        else:
            raise IllegalAccessException
    
    #searches note according to code        
    def search_note(self, code: int) -> Note:
        if self.is_logged:
            if self.patient_dao.cur_patient:
                return self.patient_dao.cur_patient.search_note(code)
            else:
                raise NoCurrentPatientException
        else:
            raise IllegalAccessException
    
    #returns notes that contains a specific string in a list        
    def retrieve_notes(self, text: str) -> list:
        if self.is_logged:
            if self.patient_dao.cur_patient:
                return self.patient_dao.cur_patient.retrieve_notes(text)
            else:
                raise NoCurrentPatientException
        else:
            raise IllegalAccessException
    
    #updates note according to the code and text given
    def update_note(self, code: int, new_text: str) -> bool:
        if self.is_logged:
            if self.patient_dao.cur_patient:
                return self.patient_dao.cur_patient.update_note(code, new_text)
            else:
                raise NoCurrentPatientException
        else:
            raise IllegalAccessException
    
    #deletes a note
    def delete_note(self, code: int) -> bool:
        if self.is_logged:
            if self.patient_dao.cur_patient:
                return self.patient_dao.cur_patient.delete_note(code)
            else:
                raise NoCurrentPatientException
        else:
            raise IllegalAccessException
        
    #lists all the notes that current patient has
    def list_notes(self) -> list:
        if self.is_logged:
            if self.patient_dao.cur_patient:
                return self.patient_dao.cur_patient.list_notes()
            else:
                raise NoCurrentPatientException
        else:
            raise IllegalAccessException
