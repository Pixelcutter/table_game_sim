from Shoe import Shoe
import models
import random
from Baccarat import Baccarat


def main():
    number_of_decks = 8
    shoe = Shoe(number_of_decks)
    baccarat = Baccarat(shoe)

    for i in range(10):
        print(f"Game {i}")
        baccarat.play()
        baccarat.print_board()
        baccarat.reset_game()


if __name__ == "__main__":
    main()
