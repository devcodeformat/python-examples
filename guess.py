# This is a Guess the Number game.
# Importing 'random' module to use 'randint()' function
import random

# Variable for user set to 0; no guesses made
guessesTaken = 0

# Displays string to user
print('Hello! What is your name?')
# User input is placed in 'myName' variable
myName = input()

# 'random' module's 'randint()' function assigned to 'number'
# 'number' variable is what the user is attempting to guess
number = random.randint(1, 20)

# Displays user's name (or what was inputted) with predefined string
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

# Starting at [ for 0 (guessesTaken) in range(6): ] 
for guessesTaken in range(6):
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')