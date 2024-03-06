from Shoe import Shoe

class Baccarat:
	''' docstring for Baccarat '''
	def __init__(self, shoe: Shoe):
		self.shoe = shoe
		self.board = {
			"player": 0,
			"banker": 0,
			"tie": 0,
			"display": [[None for _ in range(80)] for _ in range(8)]
		}
		self.players = []
	
	def prepare_shoe(self):
		self.shoe.shuffle_and_cut()
		self.shoe.insert_cut_card()

	def deal_hand(self):
		cards = self.shoe.deal_n_cards(4)
		banker_hand = [cards["cards"][0], cards["cards"][2]]
		player_hand = [cards["cards"][1], cards["cards"][3]]
		return {"banker": banker_hand, "player": player_hand, "cut_card": cards["cut_card"]}
	
	def score_hand(self, hand):
		score = 0
		for card in hand:
			score += card.value
		return score % 10
	
	def play_hand(self):
		hands = self.deal_hand()
		winner = None
		score = None
		banker_score = self.score_hand(hands["banker"])
		player_score = self.score_hand(hands["player"])

		if banker_score == 8 or banker_score == 9 or player_score == 8 or player_score == 9:
			winner = hands["banker"] if banker_score > player_score else hands["player"]
			if winner == hands["banker"]:
				self.board["banker"] += 1
				score = 
			score = {"banker": banker_score, "player": player_score}
		
		return {"winner": winner, "score": score, "cut_card": hands["cut_card"]}

	def play(self):
		self.prepare_shoe()
		cut_card_found = False
		last_winner = None

		while not cut_card_found:
			re = self.play_hand()
			last_winner = re["winner"]

		


