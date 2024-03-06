from Shoe import Shoe
import models
import random
from Baccarat import Baccarat


def main():
    number_of_decks = 8
    shoe = Shoe(number_of_decks)
    baccarat = Baccarat(shoe)
    baccarat.prepare_shoe()
    print(baccarat.shoe)
    baccarat.play()
    baccarat.print_board()
    print(shoe.cards_popped)


if __name__ == "__main__":
    main()
