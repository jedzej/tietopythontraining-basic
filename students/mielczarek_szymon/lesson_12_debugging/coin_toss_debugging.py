#! python3
import random

COIN_TOSS = {'tails': 0,
             'heads': 1}


def get_guess():
    guess = ''
    while guess not in (list(COIN_TOSS.keys())):
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()
    return guess


toss = random.randint(0, 1)  # 0 is tails, 1 is heads
if toss == COIN_TOSS[get_guess()]:
    print('You got it!')
else:
    print('Nope! Guess again!')
    if toss == COIN_TOSS[get_guess()]:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
