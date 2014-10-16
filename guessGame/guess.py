# This is a guess the number game.
import random
import sys

guessesTaken = 0
guessesLeft = 6

print('Welcome new player, what is your name?')
myName = input()

number = random.randint(1,20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

while guessesTaken < guessesLeft:
    print('Take a guess.') # There are four space in front of print.
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        triesLeft = str(guessesLeft - guessesTaken)
        print('Your guess is too low. ' + triesLeft + ' tries left.')

    if guess > number:
        triesLeft = str(guessesLeft - guessesTaken)
        print('Your guess it too high. ' + triesLeft + ' tries left.')

    if guess == number:
        break

if guess == number:
    guessText = str(guessesTaken)
    
    if guessesTaken <= 3 & guessesTaken > 1:
        print('Wow! You got it in only ' + guessText + ' tries! You\'re amazing at this')
        exit(0)
    if guessesTaken == 1:
        print('GET OUT OF MY HEAD ' + myName.upper())
        exit(0)
    if guessesTaken == 6:
        print('A little too close for comfort dont\'t you think ' + myName + '? You can do better than ' + guessText + ' guesses next time.')
        exit(0)
    else:
        print('Good job, ' + myName + '! You guessed my number in ' + guessText + ' tries!')
        exit(0)

if guess != number:
    number = str(number)
    print('Sorry ' + myName + ', the number I was thinking of was actually ' + number)
    exit(0)
