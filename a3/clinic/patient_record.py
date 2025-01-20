from clinic.note import *

class PatientRecord:
    def __init__(self, autocounter: int) -> None:
        self.__autocounter = autocounter
        self.__notes = {}

    #returns the current autocounter value
    def get_autocounter(self) -> int:
        return self.__autocounter
    
    #increments the autocounter by 1
    def update_autocounter(self) -> int:
        self.__autocounter += 1
        return self.__autocounter
    
    # updates the autocounter then creates a new Note class and stores in dictionary with current autocounter as key
    def create_note(self, text: str) -> Note:
        self.update_autocounter()
        temp_note = Note(self.get_autocounter(), text)
        self.__notes[self.get_autocounter()] = temp_note
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
            return True
        else:
            return False
        
    # if a Note with code as its key exists it is removed from the dictionary
    def delete_note(self, code: int) -> bool:
        if self.__notes:
            if code in self.__notes:
                self.__notes.pop(code)
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
