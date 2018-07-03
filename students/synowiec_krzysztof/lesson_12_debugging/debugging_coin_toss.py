import random
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s- %(message)s')

HEADS = 'heads'
TAILS = 'tails'
coin_sides = (HEADS, TAILS)


def main():
    guess = choose_side()
    toss = coin_sides[random.randint(0, 1)]
    logging.debug('Drawn value {}'.format(toss))
    if toss == guess:
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guess = choose_side()
        if toss == guess:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')


def choose_side():
    guess = ''
    while guess not in coin_sides:
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()
    logging.debug('Chosen value {}'.format(guess))
    return guess


if __name__ == '__main__':
    main()
