import pickle
from clinic.dao.note_dao import NoteDAO
from clinic.note import *
from clinic.exception.invalid_login_exception import InvalidLoginException
from clinic.exception.duplicate_login_exception import DuplicateLoginException
from clinic.exception.invalid_logout_exception import InvalidLogoutException
from clinic.exception.illegal_access_exception import IllegalAccessException
from clinic.exception.illegal_operation_exception import IllegalOperationException
from clinic.exception.no_current_patient_exception import NoCurrentPatientException

class NoteDAOPickle:
    def __init__ (self, NoteDAO, autosave=False, phn = None):
        self.autosave = autosave
        self.autocounter = 0
        self.__notes = {}
        self.phn = phn
        self.filename = f"clinic/records/{self.phn}.dat"        # file to store notes in as phn.dat

        if self.autosave:       #if autosave is true then the constructor will try to load data from the corresponding file in binary mode
            try:
                with open(self.filename, 'rb') as file:
                    self.__notes = pickle.load(file)
                    for note in self.__notes:       # this for loop checks for the latest created note and sets its code as the autocounter after reading from the file
                        if self.__notes[note].get_code() > self.autocounter:
                            self.autocounter = self.__notes[note].get_code()
            except(FileNotFoundError):
                self.__notes = {} 
        else:
            self.__notes = {}

    # updates the autocounter then creates a new Note class and stores in dictionary with current autocounter as key
    def create_note(self, text: str) -> Note:
            self.autocounter += 1
            temp_note = Note(self.autocounter, text)
            self.__notes[self.autocounter] = temp_note

            if self.autosave:       # if autosave is on write the notes into the file, in binary mode
                with open(self.filename, 'wb') as file:
                    pickle.dump(self.__notes, file)
            return temp_note
    
    # searches for key code in dictionary, returns Note if exists else None
    def search_note(self, code: int) -> Note:
        if code in self.__notes:
            return self.__notes[code]
        else:
            return None
        
    # searches Notes in dictionary that contain text, adds them to a list and returns that list
    def retrieve_notes(self, text: str) -> list:
        retrieved_notes = []
        for note in self.__notes:
            if text in self.__notes[note].get_text():
                retrieved_notes.append(self.__notes[note])
        return retrieved_notes

    # takes a code and new text, if a Note has the code as a key it updates the text to the new text
    def update_note(self, code: int, text: str) -> bool:
        if self.__notes:
            self.__notes[code].set_text(text)

            if self.autosave:       # if autosave is on write the notes into the file, in binary mode
                with open(self.filename, 'wb') as file:
                    pickle.dump(self.__notes, file)
            return True
        else:
            return False
        
    # if a Note with code as its key exists it is removed from the dictionary
    def delete_note(self, code: int) -> bool:
        if self.__notes:
            if code in self.__notes:
                self.__notes.pop(code)

                if self.autosave:       # if autosave is on write the notes into the file, in binary mode
                    with open(self.filename, 'wb') as file:
                        pickle.dump(self.__notes, file)
                return True
        else:
            return False

    # places all notes into a list with the first index being the latest note and returns the list
    def list_notes(self) -> list:
        notes_list = []
        if self.__notes:
            for code in reversed (self.__notes):
                notes_list.append(self.__notes[code])
        return notes_list
