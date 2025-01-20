from clinic.patient_record import *
from clinic.note import *
class Patient:
    def __init__(self, phn: int, name: str, birth_date: str, phone: str, email: str, address: str ) -> None:
        self.__phn = phn
        self.__name = name
        self.__birth_date = birth_date
        self.__phone = phone
        self.__email = email
        self.__address = address
        self.__patient_record = PatientRecord(0)

    #To String Function
    def __str__(self):
       return f"Patient: {self.get_phn()}\nName: {self.get_name()}\nBirthday: {self.get_birth_date()}\nPhone Number: {self.get_phone()}\nEmail: {self.get_email()}\nAddress: {self.get_address()}"

    # Getters, return corresponding patient parameters
    def get_phn(self) -> int:
        return self.__phn
    def get_name(self) -> str:
        return self.__name
    def get_birth_date(self) -> str:
        return self.__birth_date
    def get_phone(self) -> str:
        return self.__phone
    def get_email(self) -> str:
        return self.__email
    def get_address(self) -> str:
        return self.__address

    #Setters, update corresponding patient parameters
    def set_phn(self, new_phn: int) -> None:
        self.__phn = new_phn
    def set_name(self, new_name: str) -> None:
        self.__name = new_name
    def set_birth_date(self, new_birth_date: str) -> None:
        self.__birth_date = new_birth_date
    def set_phone(self, new_phone: str) -> None:
        self.__phone = new_phone
    def set_email(self, new_email: str) -> None:
        self.__email = new_email
    def set_address(self, new_address: str) -> None:
        self.__address = new_address
   
    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if type(self) != type(other):
            return False
        return self.__phn == other.__phn and self.__name == other.__name and self.__birth_date == other.__birth_date and self.__phone == other.__phone and self.__email == other.__email and self.__address == other.__address

    #Functions that work with notes through patient record
    def create_note(self, text: str) -> Note:
        return self.__patient_record.create_note(text)

    def search_note(self, code: int) -> Note:
        return self.__patient_record.search_note(code)
    
    def retrieve_notes(self, text: str) -> list:
        return self.__patient_record.retrieve_notes(text)
    
    def update_note(self, code: int, text: str) -> bool:
        return self.__patient_record.update_note(code, text)
    
    def delete_note(self, code: int) -> bool:
        return self.__patient_record.delete_note(code)
    
    def list_notes(self) -> list:
        return self.__patient_record.list_notes()

