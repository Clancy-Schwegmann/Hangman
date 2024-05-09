
#import random and regular expression so we can use those functions.
import random
import re
#main game loop check.
gameLoop = "true"
print("Welcome to Hangman")
def restartCheck():
	global userInput
	global breakLoop
	breakLoop = 0
	#Check if user wants to keep playing, with input validation.
	userInput = input ("Would you like to play again? (y/n)")
	while breakLoop == 0:
		if userInput == "y":
			breakLoop = "1"
		elif userInput == "n":
			print('''Game Over, Thanks for playing!''')
			exit()
		else:
			print("Invalid input, please enter either y or n, case sensitive.")
			userInput = input()

#Initializes the hangman word using a list.
def hangmanInit():
	loopCheck = 0
	wordSet = [""]
	
    #Store category as input.
	initInput = input("Type a category in the console, then hit enter to get started. \nCategories: fruits, kitchen products, tools, insects, animals\n")
	
    #Choose hangman word based on category input.
	while loopCheck == 0:
		loopCheck = 1
		if initInput == "fruits":
			wordSet = ["apple", "pear", "peach", "berry", "orange"]
		elif initInput == "kitchen products":
			wordSet = ["blender","spoon","knife","pan","mixer","oven"]
		elif initInput == "tools":
			wordSet = ["drill","screw","nail","cable","wrench","hammer"]
		elif initInput == "insects":
			wordSet = ["beetle","ant","fly","tick","wasp","flea"]
		elif initInput == "animals":
			wordSet = ["fox","badger","lynx","puma","lion","rabbit"]
		else:
			print("Invalid entry, try again.")
			initInput = input()
			loopCheck = 0
	

    #Declare global variables to be used outside the function.
	global guessCount
	global boolList
	global hangmanWord
	global guessList
	guessCount = 5
	boolList = []
	hangmanWord = ""
	guessList = []
	
	
	#Pick a word based on the number of items
	#in the word set, we subtract 1 because the first element is element 0.
	randomNum = random.randint(0, len(wordSet)-1)
	
	#print(wordSet[randomNum])
	hangmanWord = wordSet[randomNum]
	#loop through word length display how many
	# letters there are.
	
	hangmanOutput = ""#displays word to user.
	#Loop through each letter in word.
	for i in hangmanWord:
		hangmanOutput += "_ "
		boolList.append("_")
	
	#main loop starts here.
	#display output depending on bool statement.
		
	print(hangmanOutput)
	hangmanOutput = ""

while gameLoop == "true":
	hangmanInit()
	
	while guessCount != 0:
		letterInput = input ("Please enter one letter.")
		letterCount = len(letterInput)
		
		invalidLetter = "false"
		#search list, and check if letter equals anything
		for i in guessList:
            #make sure they don't re-guess the same letter more than once.
			if letterInput == i:
				print("You already guessed this letter, try a different one.")
				print("Here is a list of letters you have already guessed.")
				print(guessList)
				invalidLetter = "true"
				break
		if invalidLetter == "true":
				continue
				
		#Make sure input is a letter, if not then we count it as invalid input.
		regexOutput = re.search( r"([a-z])" ,letterInput)
		
		if regexOutput == None or letterCount != 1:
			print("You must only enter one letter, no spaces,try again.")
			continue
		
		#make list keeping track of all correct letters.
		lettersFound = 0
		#store letters found in boolean list.
		i = 0
		currentLetter = ""
		
		hangmanOutput = ""
		underscoreCount = 0
		
		guessList.append(letterInput)
		
		while i < len(hangmanWord):	
			currentLetter = hangmanWord[i]
			if letterInput == currentLetter:
				lettersFound += 1
				#check index, add to it.
				boolList[i] = currentLetter
			if boolList[i] == currentLetter:
				hangmanOutput += currentLetter + " "
			else:
				hangmanOutput += "_ "
				underscoreCount += 1
			i += 1
					
		#Print guess count. (ascii face)	
		if lettersFound == 0:
			guessCount -= 1
			if guessCount > 0:
				print("Incorrect letter, guesses left: " + str(guessCount))
			if guessCount == 4:
				print("(")
			elif guessCount == 3:
				print("(   )")
			elif guessCount == 2:
				print("(x  )")
			elif guessCount == 1:
				print("(x x)")
			elif guessCount == 0:
				print("(x_x) You Lose. ")
				print("The correct word is " + hangmanWord)
				restartCheck()
				continue
				
		print(hangmanOutput)
		#Check how many letters have been guessed, if the whole word is guessed, we end the game.
		if underscoreCount == 0:
			guessCount = 0
			print("You Win! :)")
			print("The final word is " + hangmanWord)
			restartCheck()
			continue