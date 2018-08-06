#!/usr/bin/env python3


import random


guess = ''
while guess not in ('heads', 'tails'):
    guess = input('Guess the coin toss! Enter heads or tails:\n')

toss = random.randint(0, 1)  # 0 is tails, 1 is heads
if toss:
    toss = 'heads'
else:
    toss = 'tails'

if toss == guess:
    print('You got it!')
else:
    guess = input('Nope! Guess again!\n')
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
