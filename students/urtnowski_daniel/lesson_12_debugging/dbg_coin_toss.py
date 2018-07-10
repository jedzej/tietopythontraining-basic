#!/usr/bin/env python3

"""
dbg_coin_toss.py: a practice project: "Debugging Coin Toss" from:
https://automatetheboringstuff.com/chapter10/

The file contains corrected version of coin toss guessing game.

"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


import random


OPTIONS = ['tails', 'heads']


def get_user_input():

    guess = ''

    while guess not in OPTIONS:
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()

    return guess


def main():

    guess = get_user_input()
    toss = random.randint(0, 1)  # 0 is tails, 1 is heads

    if OPTIONS[toss] == guess:
        print('You got it!')

    else:
        print('Nope! Guess again!')
        guess = get_user_input()

        if OPTIONS[toss] == guess:
            print('You got it!')

        else:
            print('Nope. You are really bad at this game.')


if __name__ == '__main__':
    main()
