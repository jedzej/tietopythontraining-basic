import random
import logging

logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s- %(message)s')

guess = ''

toss_int = random.randint(0, 1)  # 0 is tails, 1 is heads
if toss_int == 0:
    toss = "heads"
else:
    toss = "tails"

logging.debug("toss = " + str(toss))

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')