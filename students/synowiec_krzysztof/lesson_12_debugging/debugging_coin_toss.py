import random
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s- %(message)s')

HEADS = 'heads'
TAILS = 'tails'


def main():
    guess = ''
    while guess not in (HEADS, TAILS):
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()
    toss = random.randint(0, 1)
    logging.debug('Drawn int value {}'.format(toss))
    conv_guess = convert(guess)
    logging.debug('Choosen value after conversion {}'.format(conv_guess))
    if toss == conv_guess:
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guess = input()
        conv_guess = convert(guess)
        logging.debug('Choosen value after conversion {}'.format(conv_guess))
        if toss == conv_guess:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')


def convert(guess):
    if guess == HEADS:
        return 0
    else:
        return 1


if __name__ == '__main__':
    main()
