#! python3

import random


def main():

    guess = ''
    while guess not in (int(1), int(0)):
        print('Guess the coin toss! Enter 1 for heads or 0 for tails:')
        guess = int(input())  # integer instead of string

    toss = random.randint(0, 1)  # 0 is tails, 1 is heads
    if toss == guess:
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guess = int(input())  # spelling
        if toss == guess:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')


if __name__ == "__main":
    main()
