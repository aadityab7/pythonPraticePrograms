#-----------------------------------------------------------------#
#Instructions for playing the GAME!

def print_rules():
	print("\nTo make your move and mark on board you will have to enter the number cooresponding to that block : ")
	print("\nThe Tic tak toe grid is represeneted by numbers as follows : ")
	print()
	print(" 7 | 8 | 9 ")
	print("---+---+---")
	print(" 4 | 5 | 6 ")
	print("---+---+---")
	print(" 1 | 2 | 3 ")

#-----------------------------------------------------------------#
#Take Player names:

def player_name_1():
	player_1_name = input("\nPlayer 1 : Please enter your name : ")
	return player_1_name

def player_name_2():
	player_2_name = input("\nPlayer 2 : Please enter your name : ")
	return player_2_name 

#-----------------------------------------------------------------#
#Take player one and two signs (O or X):

def player_sign_1():
	player_1_sign = "INITIAL VALUE"

	while player_1_sign not in ["O", "X"]:
		player_1_sign = input(f"\nPlayer 1 : {player_1_name} : Do you want to be 'O or X' : ").upper()

		if player_1_sign not in ["O", "X"]:
			print("\nSorry ! Please enter a valid choice : (O or X)")

	return player_1_sign

def player_sign_2(player_1_sign):
	player_2_sign = "O"
	if player_1_sign == "O":
		player_2_sign = "X"
	return player_2_sign

#-----------------------------------------------------------------#
#function to choose who will play first:

from random import randint

def choose_first_chance():
	flip = randint(0,1)

	if flip == 0:
		return "X"
	else:
		return "O"

#-----------------------------------------------------------------#
#display the player points:

def display_points():
	print()
	print(f"Score of - {player_1_name} : {player_1_points}")
	print(f"Score of - {player_2_name} : {player_2_points}")

#-----------------------------------------------------------------#
#display the board as a grid:

def display_board():
	count = 1
	
	print("\n")
	for item in game_list:
		print(" " + item + " ", end = '')
		if count % 3 == 0:
			print()
			if count < 8:
				print("---+---+---")
		else:
			print("|", end = "")
		count += 1

#-----------------------------------------------------------------#
#function to ask the user for the next move:
def your_chance():
	if player_1_sign == current_chance:
		curr = player_1_name
	else:
		curr = player_2_name

	print(f"\nIt is your chance : {curr} ({current_chance})")

#-----------------------------------------------------------------#
#Function to check if current game completed : 
def is_game_over():
	
	for i in range(0, 9, 3):
		if(game_list[i] == game_list[i + 1] == game_list[i + 2] == current_chance):
			return True

	for i in range(0, 3):
		if(game_list[i] == game_list[i + 3] == game_list[i + 6] == current_chance):
			return True

	if(game_list[0] == game_list[4] == game_list[8] == current_chance):
		return True
	elif(game_list[2] == game_list[4] == game_list[6] == current_chance):
		return True

	return False

#-----------------------------------------------------------------#
#Taking user input on board:
def user_mark_on_board():
	your_chance()
	user_input = 753
	while user_input not in ['1','2','3','4','5','6','7','8','9']:
		user_input = input(f"Please enter a number between (1 - 9) on to mark {current_chance} on board : ")

	user_input = int(user_input)
	if (user_input) in [1, 2, 3]:
		user_input = user_input + 5
	elif user_input in [4, 5, 6]:
		user_input = user_input - 1
	else:
		user_input = user_input - 7

	return user_input

#-----------------------------------------------------------------#
#Taking user input on board:
def play_next_move(game_list):
	
	valid_input = False

	user_input = user_mark_on_board()

	if game_list[user_input] == " ":
		valid_input = True

	while(valid_input == False):
		print("\nSorry ! That place on board is already taken, please select an empty block!")
		user_input = user_mark_on_board()
		if(user_input in range(0,10)):
			valid_input = True

	game_list[user_input] = current_chance

	return game_list

#-----------------------------------------------------------------#
#Changing the sign after every turn:
def change_chance():
	if current_chance == "X":
		return "O"
	else:
		return "X"

#-----------------------------------------------------------------#
#Print player who is currently Winning:

def currently_winning():
	if player_1_points > player_2_points:
		print(f"\nCurrently Player 1 : {player_1_name} is WINNING !!")
	elif player_1_points < player_2_points:
		print(f"\nCurrently Player 2 : {player_2_name} is WINNING !!")
	else:
		print("\nCurrently the GAME is TIED !")

#-----------------------------------------------------------------#
#function to ask the user if they want to keep playing:

def is_game_on():
	user_input_for_game_on = "INITIAL VALUE"
	while user_input_for_game_on not in ["Y", "N", "y", "n"]:
		user_input_for_game_on = input("\nDo you want to continue playing : (Y / y or N / n) : ")

	if user_input_for_game_on in ["Y", "y"]:
		return True
	else:
		return False

#-----------------------------------------------------------------#
#Execution on Program : 

print("\nHello! Welcome to the Python Tic Tac Toe Game by Aaditya")
print_rules()

game_on = True

player_1_name = player_name_1()
player_2_name = player_name_2()
player_1_points = 0
player_2_points = 0


#Run While Game is ON ! 
while game_on:
	
	# create a list corresponding to all 9 blocks in tic tac toe
	game_list = [' '] * 9
	counter = 0
	is_over = False
	current_chance = choose_first_chance()

	player_1_sign = player_sign_1()
	player_2_sign = player_sign_2(player_1_sign)
	
	#displaying info on screen
	display_points()
	display_board()
	
	while not is_over:
		
		if counter == 9:
			is_over = True
			print("\nTHIS GAME IS A TIE !")
		else:
			game_list = play_next_move(game_list)
			is_over = is_game_over()
			
			if is_over == True:
				if player_1_sign == current_chance:
					print(f"\nPlayer 1 : {player_1_name} WON this GAME !!")
					player_1_points += 1
				else:
					print(f"\nPlayer 2 : {player_2_name} WON this GAME !!")
					player_2_points += 1

			display_points()
			display_board()
			current_chance =  change_chance()

		counter += 1

	currently_winning()
	game_on = is_game_on()