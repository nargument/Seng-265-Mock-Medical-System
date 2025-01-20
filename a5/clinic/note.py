from datetime import datetime
class Note:
    def __init__(self, code: int, text: str) -> None:
        self.code = code
        self.text = text
        self.timestamp = datetime.now()

    def get_code(self,) -> int:
        return self.code
    def get_text(self) -> str:
        return self.text
    
    def set_text(self, text: str) -> None:
        self.text = text
    
    def __eq__(self, other):
        if self is other:
            return True
        if type(self) != type(other):
            return False
        return self.text == other.text and self.code == other.code