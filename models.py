from dataclasses import dataclass

@dataclass
class Card:
    suit: str
    value: str

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def __repr__(self):
        return f"{self.value} of {self.suit}"


