from clinic.note import *
from clinic.dao.note_dao_pickle import *
from clinic.dao.note_dao import *

class PatientRecord:
    def __init__(self, autosave = False, phn = None) -> None:
        self.autosave = autosave
        self.phn = phn
        self.note_dao = NoteDAOPickle(NoteDAO, self.autosave, self.phn)
    
    # updates the autocounter then creates a new Note class and stores in dictionary with current autocounter as key
    def create_note(self, text: str) -> Note:
        return self.note_dao.create_note(text)

    # searches for key code in dictionary, returns Note if exists else None
    def search_note(self, code: int) -> Note:
        return self.note_dao.search_note(code)
    
    # searches Notes in dictionary that contain text, adds them to a list and returns that list
    def retrieve_notes(self, text: str) -> list:
        return self.note_dao.retrieve_notes(text)
    
    # takes a code and new text, if a Note has the code as a key it updates the text to the new text
    def update_note(self, code: int, text: str) -> bool:
        return self.note_dao.update_note(code, text)
        
    # if a Note with code as its key exists it is removed from the dictionary
    def delete_note(self, code: int) -> bool:
        return self.note_dao.delete_note(code)

    # places all notes into a list with the first index being the latest note and returns the list
    def list_notes(self) -> list:
        return self.note_dao.list_notes()
