from models import Card
import random

# NEED TO CHANGE HOW FINAL CUT WORKS, NEED A RED CUT CARD INSERTED IN THE SHOE AND WHEN IT APPEARS, THE SHOE IS CHANGED

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
    "A": 1
}

class Shoe:
    def __init__(self, number_of_decks, exlude_cards=[]):
        self.discards = []
        self.number_of_decks = number_of_decks
        self.exluded_cards = exlude_cards
        self.build_shoe()

    def build_shoe(self):
        self.cards = []
        for _ in range(self.number_of_decks):
            for suit in suits:
                for card, value in cards.items():
                    if card not in self.exluded_cards:
                        self.cards.append(Card(suit, card, value))

    def count(self):
        return len(self.cards)
    
    def shuffle(self):
        random.shuffle(self.cards)

    def shuffle_and_cut(self):
        self.shuffle()
        self.cut()

    def final_cut(self):
        cut_point = self.count() // 2 if self.number_of_decks <= 2 else cards_per_deck
        self.discards = self.cards[:cut_point]
        self.cards = self.cards[cut_point:]

    def cut(self):
        if self.number_of_decks <= 2:
            cut_point = random.randint(26, len(self.cards) - 26)
        else:
            cut_point = random.randint(cards_per_deck, len(self.cards) - cards_per_deck)
        
        self.cards = self.cards[cut_point:] + self.cards[:cut_point]

    def __str__(self):
        return f"Shoe of {self.number_of_decks} deck(s) and {len(self.cards)} cards"

    def __repr__(self):
        return f"Shoe of {self.number_of_decks} deck(s) and {len(self.cards)} cards"