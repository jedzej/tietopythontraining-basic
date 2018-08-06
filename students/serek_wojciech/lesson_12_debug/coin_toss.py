#!/usr/bin/env python3
"""Coin toss exercise"""
import random

OPTIONS = ('heads', 'tails')


def get_user_input():
    """Get input from user"""
    guess = ''
    while guess not in OPTIONS:
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()
    return guess


def main():
    """Main function"""

    guess = get_user_input()
    toss = random.choice(OPTIONS)
    if toss == guess:
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guess = get_user_input()
        if toss == guess:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')


if __name__ == "__main__":
    main()
