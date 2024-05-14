from dataclasses import dataclass

@dataclass
class Country:
    CCode: int
    StateAbb: str
    StateNme: str

    def __hash__(self):
        return hash(self.CCode)

    def __str__(self):
        return f"{self.CCode} - {self.StateNme}"
