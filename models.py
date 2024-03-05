from dataclasses import dataclass

@dataclass
class Card:
    suit: str
    value: int
    card: str

    def __str__(self):
        return f"{self.card} {self.suit}"

    def __repr__(self):
        return f"{self.card} {self.suit}"


