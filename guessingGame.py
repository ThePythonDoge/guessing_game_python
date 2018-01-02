#Game to guess arandom number

def numbergame():
	magic_number = 7
	user_number = input("Pick a number between 1-10: ")
	if int(user_number)== magic_number:
		print("You won! You picked {}".format(user_number))
	else:
		print("You picked {}, you lost! Play again".format(user_number))
        # Run again if user lost
		numbergame()

numbergame()
