from datetime import datetime
class Note:
    def __init__(self, code: int, text: str) -> None:
        self.__code = code
        self.__text = text
        self.__timestamp = datetime.now()

    def get_code(self, code: int) -> int:
        return self.__code
    def get_text(self) -> str:
        return self.__text
    
    def set_text(self, text: str) -> None:
        self.__text = text
    
    def __eq__(self, other):
        if self is other:
            return True
        if type(self) != type(other):
            return False
        return self.__text == other.__text and self.__code == other.__code