import logging
import random

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s '
                                                '- %(message)s')

coin_sides = ["tails", "heads"]


def user_coin_toss():
    guess = ''
    while guess not in coin_sides:
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()
    logging.debug('User coin toss value: {0}'.format(guess))
    return guess


def main():
    """Random coin toss"""
    random_coin_toss = random.randint(0, 1)
    logging.debug('Random coin toss value: {0}({1})'
                  .format(random_coin_toss, coin_sides[random_coin_toss]))

    """User coin toss"""
    if coin_sides[random_coin_toss] == user_coin_toss():
        print('You got it!')
        logging.debug('End game: User guessed!')
    else:
        print('Nope! Guess again!')
        if coin_sides[random_coin_toss] == user_coin_toss():
            print('You got it!')
            logging.debug('End game: User guessed!')
        else:
            print('Nope. You are really bad at this game.')
            logging.debug('End game: User did not guess!')


if __name__ == '__main__':
    main()
