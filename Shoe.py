import models
import random

# NEED TO CHANGE HOW FINAL CUT WORKS, NEED A RED CUT CARD INSERTED IN THE SHOE AND WHEN IT APPEARS, THE SHOE IS CHANGED


class Shoe:
    def __init__(self, number_of_decks, exlude_cards=[]):
        self.number_of_decks = number_of_decks
        self.exluded_cards = exlude_cards
        self.build_shoe()

    def build_shoe(self):
        self.cards = []
        for _ in range(self.number_of_decks):
            for suit in models.suits:
                for card, value in models.cards.items():
                    if card not in self.exluded_cards:
                        self.cards.append(models.Card(suit, value, card))

    def reset_shoe(self):
        self.build_shoe()

    def count(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_n_cards(self, number_of_cards):
        cards = []

        for _ in range(number_of_cards):
            card = self.cards.pop()
            if card is None:
                card = self.cards.pop()
            cards.append(card)

        return cards

    def shuffle_and_cut(self, cut_point=0):
        self.shuffle()
        self.cut(cut_point)

    def cut(self, cut_point=None):
        self.cards = self.cards[cut_point:] + self.cards[:cut_point]

    def __str__(self):
        return f"Shoe of {self.number_of_decks} deck(s) and {len(self.cards)} cards"

    def __repr__(self):
        return f"Shoe of {self.number_of_decks} deck(s) and {len(self.cards)} cards"
