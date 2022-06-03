from random import shuffle

suits = ("Hearts", "Club", "Spades", "Diamond")
ranks = ("two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace")
values = {"two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9, "ten" : 10, "jack": 10, "queen" : 10, "king" : 10, "ace" : 11}


#create a class for cards:

class Card:
	'''
	Class to define and store info about the cards
	'''

	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		self.value = values[rank]

	def __str__(self):
		return f"{self.rank} of {self.suit}"


#create a player class - name , bankroll

class Player:
	'''
	The Class to define and store info of the players
	the methods to add and remove cards to and from the hand
	'''

	def __init__(self, name, bankroll = 0):
		self.name = name
		self.bankroll = bankroll
		self.all_cards = []

	def add_to_hand(self, card_s):
		if type(card_s) == type([]):
			self.all_cards.extend(card_s)
		else:
			self.all_cards.append(card_s)

	def game_lost(self, bet):
		self.bankroll -= bet

	def game_won(self, bet):
		self.bankroll += bet * 2

#create deck class - to create a deck and impliment distribution
class Deck:
	'''
	Defining and storing the deck of cards
	'''

	def __init__(self):
		
		self.all_cards = []

		for suit in suits:
			for rank in ranks:
				new_card = Card(suit, rank)
				self.all_cards.append(new_card)

	def shuffle_deck(self):
		shuffle(self.all_cards)

	def hand_one(self):
		return self.all_cards.pop()

#function to take the amount they want to bet		
def take_bet(player1):
	bet = player1.bankroll + 1
	while bet > player1.bankroll:
		bet = input("\nPlease Enter the amount of money you want to BET : ")

		if bet.isdigit():
			bet = float(bet)
			if bet > player1.bankroll:
				print(f"\nSorry ! You only have {player1.bankroll}")
		else:
			print("Please enter a valid number")
			bet = player1.bankroll + 1

	return bet

#input the amount of money user have 
def take_bankroll():
	bankroll = "Invalid"
	while not bankroll.isdigit():
		bankroll = input("\nPlease enter the amount of money you have : ")

		if not bankroll.isdigit():
			print("Please enter a valid Number")

	return float(bankroll)

#function to calculate the sum of cards in hand
def sum_of_cards(cards):
	card_sum = 0

	for card in cards:
		card_sum += card.value

	return card_sum

#function to ask user is the game on (does they want to play again)
def is_game_on():
	yes_or_no = input("\nDo you want to play again?? (Y / N) : ").upper()
	if(yes_or_no == "Y"):
		return True
	else:
		return False

#to display the score of player and card of dealer
def show_score(player_sum, player_cards, dealer_cards):
	print("\nYour cards : ")
	for card in player_cards:
		print(f"{card} - ({card.value})")
	print(f"Your total : {player_sum}")
	print(f"Dealer's Card : {dealer_cards[0]} ({dealer_cards[0].value})")

def won(player1):
	print("\nCongratulations !! You WON !! :)")	
	player1.game_won(bet)

def lost(player1):
	print("\nSorry ! You Lost :(")
	player1.game_lost(bet)


#INTRO --------------------------------------------------------------------
print("\nHello ! Welcome to the game of BlackJack by Aaditya Bansal !!!\n")

player_name = input("Please Enter your name : ")
bankroll = take_bankroll()

player1 = Player(player_name, bankroll)

#Game Logic ---------------------------------------------------------------
game_on = True

while game_on:

	print(f"\n{player1.name} - Your balance is : {player1.bankroll} ")

	player_sum = 0
	dealer_sum = 0
		
	game_deck = Deck()
	game_deck.shuffle_deck()

	player_cards = []
	dealer_cards = []

	player_cards.append(game_deck.hand_one())
	player_cards.append(game_deck.hand_one())

	dealer_cards.append(game_deck.hand_one())
	dealer_cards.append(game_deck.hand_one())

	player_sum = sum_of_cards(player_cards)
	dealer_sum = sum_of_cards(dealer_cards)

	
	bet = take_bet(player1)
	

	#Player's Turn
	#stay or hit :
	hitting = True

	while hitting:

		show_score(player_sum, player_cards, dealer_cards)

		if(player_sum > 21):
			hitting = False
			lost(player1)
			break
		if player_sum == 21:
			hitting = False
			won(player1)
			break

		hit_or_stay = "Initial Input"

		while hit_or_stay not in ["H", "S"]:
			hit_or_stay = input("\nEnter (H) to hit (take another card) and (S) to stay : ").upper()

		if hit_or_stay == "H":
			#Logic for picking another card
			player_cards.append(game_deck.hand_one())
			player_sum = sum_of_cards(player_cards)
		else:
			hitting = False
			break

	#Dealer's Turn
	if player_sum < 21:
		show_score(player_sum, player_cards, dealer_cards)
		while dealer_sum < 21:
			dealer_cards.append(game_deck.hand_one())
			dealer_sum = sum_of_cards(dealer_cards)
			if dealer_sum > player_sum and dealer_sum <= 21:
				lost(player1)
				break
		else:
			won(player1)

	#Output at end of game : 
	print(f"\nFinal Score : {player_name} : {player_sum} and Dealer : {dealer_sum}")
	print(f"\n{player1.name} - Now, Your balance is : {player1.bankroll} ")
	game_on = is_game_on()