"""
The following program is meant to be a simple coin toss
guessing game. The player gets two guesses (it’s an easy
game). However, the program has several bugs in it.
Run through the program a few times to find the bugs
that keep the program from working correctly.
"""

import logging
import random

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s '
                    '- %(levelname)s - %(message)s')

GUESS_COUNT = 2
options = {0: "tails", 1: "heads"}


def guess_coin_toss(count):
    for i in range(count):
        guess = input()
        logging.debug("User input: " + guess)
        print('Guess the coin toss! Enter heads or tails:')
        toss = random.randint(0, 1)

        logging.debug("toss: " + options[toss])
        if options.get(toss) == guess:
            print('You got it!')
            return
        else:
            if i != count - 1:
                print('Nope! Guess again!')
            else:
                print('Nope. You are really bad at this game.')


def main():
    logging.debug('main():')
    guess_coin_toss(GUESS_COUNT)


if __name__ == '__main__':
    main()
