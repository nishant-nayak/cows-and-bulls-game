import random

def makeList(num):		#Converting a number to a list of digits
	guess=[]
	while num>0:
		n=num%10
		guess.insert(0,n)
		num=int(num/10)
	while len(guess) < 4:
		guess.insert(0,0)
	return guess

def printRules():		#Printing out the rules of the game
	msg="\n\nThere is a secret 4 digit code, with no repeating digits"
	msg+=" that you have to guess!\nFor every number you guess, if a "
	msg+="digit is in the secret code, and is in the correct position, "
	msg+="you get one cow.\nIf the digit is in the secret code but is in"
	msg+=" the wrong position, you get a bull."
	print(msg)
	
def checkInput(num):		#Checking for invalid input
	if not num.isnumeric():
		print("Please enter a 4 digit number.\n")
		return True
	numList=makeList(int(num))
	if len(numList) > 4:
		print("Please enter a 4 digit number.\n")
		return True
	for i in numList:
		if numList.count(i) > 1:
			print("Please enter a 4 digit number without duplicate digits.\n")
			return True
	return False
	
print("Welcome to the Cows and Bulls Game!");
printRules()

while True:				#Main Game Running Loop
	print("\n\nGood Luck!\n\n\n")
	target=[]
	while len(target) < 4:
		n = random.randint(0,9)
		if n not in target:
			target.append(n)
			
	guesses=0
	while True:				#Loop for checking each Guess
		cows,bulls=0,0
		num=input("Enter a number:\n>>> ")
		if checkInput(num):
			continue
		numList=makeList(int(num))
		
		if target == numList:
			print("You guessed it right!")
			break
		for i in range(0,4):
			if numList[i] in target:
				if numList[i] == target[i]:
					cows+=1
				else:
					bulls+=1
		print(str(cows) + " cows, " + str(bulls) + " bulls\n")
		guesses+=1

	print("You took " + str(guesses) + " guesses!")
	flag=input("\n\nPress q to quit, or any other key to keep playing!: ")
	if flag.lower() == 'q':
		break

print("\nThanks for Playing!")

