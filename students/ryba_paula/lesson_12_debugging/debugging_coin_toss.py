import random
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s '
                                                '- %(message)s')

guess_array = ['heads', 'tails']
guess = ''
toss = random.choice(guess_array)
logging.debug(toss)

while guess not in guess_array:
    guess = input('Guess the coin toss! Enter heads or tails: ')

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
