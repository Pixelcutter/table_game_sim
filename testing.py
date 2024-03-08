from Shoe import Shoe
import models
import random
from Baccarat import Baccarat
import sys


def main():
    number_of_decks = 8
    shoe = Shoe(number_of_decks)
    baccarat = Baccarat(shoe)
    times_won = 0
    times_lost = 0

    if len(sys.argv) > 1:
        max_win_count = int(sys.argv[1])
        max_loss_count = int(sys.argv[2])
        n_hands = int(sys.argv[3])
    else:
        max_win_count = int(input("How many wins do you want to achieve? "))
        max_loss_count = int(input("How many losses until you stop? "))
        n_hands = int(input("How many hands do you want to play? "))

    for i in range(n_hands):
        baccarat.play()

        budget = 500
        base_bet = 25
        current_bet = base_bet
        current_winner = "B"
        loss_count = 0
        win_count = 0
        x, y = 0, 0
        display = baccarat.board["display"]

        jumps = []

        while display[0][x] != " ":
            if display[y][x] == current_winner:
                budget += current_bet
                win_count += 1
                loss_count = 0
                current_bet = base_bet
            elif display[y][x] != current_winner and display[y][x] != "T":
                budget -= current_bet
                current_bet = current_bet * 2
                loss_count += 1
                # if loss_count == max_loss_count - 1:
                #     print(f"current_winner: {current_winner}, x: {x}, y: {y}")
                #     current_winner = display[0][x - 1]
                #     print(f"Current Winner: {current_winner}", 0, x - 1)
                # else:
                #     current_winner = display[y][x]
                current_winner = display[y][x]

            if loss_count == max_loss_count or win_count == max_win_count:
                break

            y += 1
            if y >= len(display) or display[y][x] == " ":
                y = 0
                x += 1

        if loss_count == max_loss_count:
            times_lost += 1
        else:
            times_won += 1

        # print(f"Budget: {budget}") if budget < 0 else None
        if loss_count == 5:
            print("Lost")
            print(f"Loss Count: {loss_count}, Win Count: {win_count}")
            baccarat.print_board()
            print(jumps)
        baccarat.reset_game()

    print(
        f"Times Won: {times_won}\nTimes Lost: {times_lost}\nWin Rate: {times_won / (times_won + times_lost)}"
    )

    # for i in range(10):
    #     print(f"Game {i}")
    #     baccarat.play()
    #     baccarat.print_board()
    #     baccarat.reset_game()


if __name__ == "__main__":
    main()
