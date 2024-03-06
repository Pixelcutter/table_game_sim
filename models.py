from dataclasses import dataclass
cards_per_deck = 52
suits = ["H", "D", "C", "S"]
cards = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 1,
}

@dataclass
class Card:
    suit: str
    value: int
    card: str

    def __str__(self):
        return f"{self.card} {self.suit}"


