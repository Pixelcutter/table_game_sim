from Shoe import Shoe
import random
import models


class Baccarat:
    """docstring for Baccarat"""

    banker_rules = {
        3: {
            1: True,
            2: True,
            3: True,
            4: True,
            5: True,
            6: True,
            7: True,
            8: False,
            9: True,
            10: True,
        },
        4: {
            1: False,
            2: True,
            3: True,
            4: True,
            5: True,
            6: True,
            7: True,
            8: False,
            9: False,
            10: False,
        },
        5: {
            1: False,
            2: False,
            3: False,
            4: True,
            5: True,
            6: True,
            7: True,
            8: False,
            9: False,
            10: False,
        },
        6: {
            1: False,
            2: False,
            3: False,
            4: False,
            5: False,
            6: True,
            7: True,
            8: False,
            9: False,
            10: False,
        },
    }

    def __init__(self, shoe: Shoe):
        self.shoe = shoe
        self.board = {
            "P": 0,
            "B": 0,
            "T": 0,
            "display": [[" " for _ in range(60)] for _ in range(80)],
        }
        self.players = []
        self.hands_left = 0

    def prepare_shoe(self):
        self.shoe.shuffle_and_cut(
            random.randint(
                models.cards_per_deck, len(self.shoe.cards) - models.cards_per_deck
            )
        )

    def deal_hand(self):
        cards = self.shoe.deal_n_cards(4)
        player_hand = [cards[0], cards[2]]
        banker_hand = [cards[1], cards[3]]
        return banker_hand, player_hand

    def score_hand(self, hand):
        score = 0
        for card in hand:
            score += card.value
        return score % 10

    def is_natural(self, score):
        return score == 8 or score == 9

    def natural_winner(self, banker_score, player_score):
        if banker_score < player_score:
            return "P", player_score
        elif banker_score > player_score:
            return "B", banker_score
        else:
            return "T", banker_score

    def play_hand(self):
        banker_hand, player_hand = self.deal_hand()
        winner = None
        score = None

        banker_score = self.score_hand(banker_hand)
        player_score = self.score_hand(player_hand)

        if self.is_natural(banker_score) or self.is_natural(player_score):
            # print(
            #     f"Player Hand: {self.print_hand(player_hand)}, Banker Hand: {self.print_hand(banker_hand)}\n"
            # )
            return self.natural_winner(banker_score, player_score)
        else:
            last_player_card = None
            if player_score <= 5:
                last_player_card = self.shoe.deal_n_cards(1)[0]
                player_hand.append(last_player_card)
                player_score = (player_score + last_player_card.value) % 10

            if banker_score <= 2 or (not last_player_card and banker_score <= 5):
                new_banker_card = self.shoe.deal_n_cards(1)[0]
                banker_hand.append(new_banker_card)
                banker_score = (banker_score + new_banker_card.value) % 10
            elif last_player_card and banker_score != 7:
                if self.banker_rules[banker_score][last_player_card.value]:
                    new_banker_card = self.shoe.deal_n_cards(1)[0]
                    banker_hand.append(new_banker_card)
                    banker_score = (banker_score + new_banker_card.value) % 10

        if player_score > banker_score:
            winner = "P"
            score = player_score
        elif player_score < banker_score:
            winner = "B"
            score = banker_score
        else:
            winner = "T"
            score = player_score

        self.hands_left -= 1

        # print(
        #     f"Player Hand: {self.print_hand(player_hand)}, Banker Hand: {self.print_hand(banker_hand)}, Winner: {winner}\n"
        # )
        return winner, score

    def print_hand(self, hand):
        s = ""
        for card in hand:
            s += f"{card}, "
        return s.rstrip(", ")

    def reset_game(self):
        self.board = {
            "P": 0,
            "B": 0,
            "T": 0,
            "display": [[" " for _ in range(60)] for _ in range(80)],
        }
        self.players = []
        self.hands_left = -1
        self.shoe.reset_shoe()

    def play(self, number_of_hands=-1):
        self.prepare_shoe()
        hands_left = number_of_hands

        last_winner, last_score = self.play_hand()
        board_x, board_y = 0, 0
        self.board["display"][board_y][board_x] = last_winner

        while self.shoe.count() >= models.cards_per_deck and hands_left != 0:
            winner, last_score = self.play_hand()
            self.board[winner] += 1

            if winner == "T":
                board_y += 1
                self.board["display"][board_y][board_x] = winner
                continue

            if winner == last_winner:
                board_y += 1
                self.board["display"][board_y][board_x] = winner
            elif winner != last_winner and last_winner is not None:
                board_x += 1
                board_y = 0
                self.board["display"][board_y][board_x] = winner

            last_winner = winner

    def print_board(self):
        max_x = self.board["display"][0].index(" ")
        print(
            f"Player: {self.board['P']}, Banker: {self.board['B']}, Tie: {self.board['T']}"
        )
        for row in self.board["display"]:
            if row.count(" ") == len(row):
                break
            for c, cell in enumerate(row):
                if c == max_x:
                    break
                print(cell, end="|")
            print()
        print()
