from Shoe import Shoe


def main():
    shoe = Shoe(1)
    shoe.shuffle_and_cut()
    shoe.insert_cut_card()
    print(shoe)
    print(shoe.cards)


if __name__ == "__main__":
    main()
