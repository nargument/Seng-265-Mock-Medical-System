from clinic.patient_record import *
from clinic.note import *
class Patient:
    def __init__(self, phn: int, name: str, birth_date: str, phone: str, email: str, address: str ,autosave = False) -> None:
        self.phn = phn
        self.name = name
        self.birth_date = birth_date
        self.phone = phone
        self.email = email
        self.address = address
        self.autosave = autosave
        self.patient_record = PatientRecord(self.autosave, self.get_phn())

    #To String Function
    def __str__(self):
       return f"Patient: {self.get_phn()}\nName: {self.get_name()}\nBirthday: {self.get_birth_date()}\nPhone Number: {self.get_phone()}\nEmail: {self.get_email()}\nAddress: {self.get_address()}"

    # Getters, return corresponding patient parameters
    def get_phn(self) -> int:
        return self.phn
    def get_name(self) -> str:
        return self.name
    def get_birth_date(self) -> str:
        return self.birth_date
    def get_phone(self) -> str:
        return self.phone
    def get_email(self) -> str:
        return self.email
    def get_address(self) -> str:
        return self.address

    #Setters, update corresponding patient parameters
    def set_phn(self, new_phn: int) -> None:
        self.phn = new_phn
    def set_name(self, new_name: str) -> None:
        self.name = new_name
    def set_birth_date(self, new_birth_date: str) -> None:
        self.birth_date = new_birth_date
    def set_phone(self, new_phone: str) -> None:
        self.phone = new_phone
    def set_email(self, new_email: str) -> None:
        self.email = new_email
    def set_address(self, new_address: str) -> None:
        self.address = new_address
   
    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if type(self) != type(other):
            return False
        return self.phn == other.phn and self.name == other.name and self.birth_date == other.birth_date and self.phone == other.phone and self.email == other.email and self.address == other.address

    #Functions that work with notes through patient record
    def create_note(self, text: str) -> Note:
        return self.patient_record.create_note(text)

    def search_note(self, code: int) -> Note:
        return self.patient_record.search_note(code)
    
    def retrieve_notes(self, text: str) -> list:
        return self.patient_record.retrieve_notes(text)
    
    def update_note(self, code: int, text: str) -> bool:
        return self.patient_record.update_note(code, text)
    
    def delete_note(self, code: int) -> bool:
        return self.patient_record.delete_note(code)
    
    def list_notes(self) -> list:
        return self.patient_record.list_notes()

