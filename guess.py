# This is a guess the number game.

import random

print('Hello. What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 20')
secretNumber = random.randint(1, 20)

for guessesTaken in range (1, 7):
	print('Take a guess.')
	guess_input = input()
	
	while not guess_input.isdigit():
		print ('Please input a number and try again')
		guess_input = input()
	
	guess = int(guess_input)
	
	if guess < secretNumber:
		print('Your guess is too low')
	elif guess > secretNumber:
		print('Your guess is too high')
	else:
		break # This condition is for the correct guess!

if guess == secretNumber:
	print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
	print('Nope, the number I was thinking of was ' + str(secretNumber))

print('You took ' + str(guessesTaken) + ' guesses.')