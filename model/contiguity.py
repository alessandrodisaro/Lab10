from dataclasses import dataclass

@dataclass
class Contiguity:
    dyad: int
    state1no: int
    state1ab: str
    state2no: int
    state2ab: str
    year: int
    conttype: int
    version: int

    def __str__(self):
        return f"confine {self.state1ab} - {self.state2ab}"
