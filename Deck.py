from models import Card

class Deck:
    def full_deck(self, exlude_values=[], number_of_decks=1):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = [
            "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"
        ]
        
        self.cards = [Card(suit, value) for suit in suits for value in values if value not in exlude_values] * number_of_decks
    
    def count(self):
        return len(self.cards)

    def __str__(self):
        return f"Deck of {len(self.cards)} cards"

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"