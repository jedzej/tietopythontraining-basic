import random
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def convert_guess_to_binary(str_guess):
    if str_guess == 'heads':
        return 0
    elif str_guess == 'tails':
        return 1
    else:
        raise Exception('Wrong function parameter')


guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
logging.debug("guess: " + guess)
toss = random.randint(0, 1)
logging.debug("toss: " + str(toss))
if toss == convert_guess_to_binary(guess):
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    logging.debug("guess: " + guess)
    if toss == convert_guess_to_binary(guess):
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
