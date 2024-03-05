from Shoe import Shoe

class Baccarat:
	''' docstring for Baccarat '''
	def __init__(self):
		self.shoe = Shoe(8)
		self.shoe.shuffle_and_cut()
		self.shoe.final_cut()
	
	def deal(self):

