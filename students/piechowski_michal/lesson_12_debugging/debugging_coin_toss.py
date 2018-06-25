#!/usr/bin/env python3

import random

guessArray = ['tails', 'heads']


def get_guess():
    guess = ''
    while guess not in guessArray:
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()

    return guess


if __name__ == "__main__":
    guess = get_guess()

    toss = random.choice(guessArray)

    if toss == guess:
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guess = get_guess()
        if toss == guess:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')


''' Original:
import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    if toss == guess:
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
'''
