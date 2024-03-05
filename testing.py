from Shoe import Shoe

def main():
	shoe = Shoe(8)
	shoe.shuffle_and_cut()
	shoe.final_cut()
	print(shoe)
	print(shoe.cards)

if __name__ == "__main__":
	main()
