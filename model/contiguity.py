from dataclasses import dataclass

@dataclass
class Contiguity:
    state1no: int
    state2no: int


    def __str__(self):
        return f"confine {self.state1no} - {self.state2no}"
