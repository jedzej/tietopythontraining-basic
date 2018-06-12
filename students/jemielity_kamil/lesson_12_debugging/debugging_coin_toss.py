import random
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

guess = ''
while guess not in ('heads', 'tails'):
    logging.debug('Guess - heads or tails')
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

if guess == 'heads':
    guess = 1
elif guess == 'tails':
    guess = 0
toss = random.randint(0, 1) # 0 is tails, 1 is heads
logging.debug('Toss value: ' + str(toss))
logging.debug('Guess value: ' + str(guess))
assert toss == 0 or toss == 1, 'toss doesn\'t contain a value of 0 or 1'
assert guess == 0 or guess == 1, 'guess doesn\'t contain a value of 0 or 1'
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    while guess not in ('heads', 'tails'):
        print('Enter value. Try again(heads or tails): ')
        guess = input()
    if guess == 'heads':
        guess = 1
    elif guess == 'tails':
        guess = 0
    logging.debug('Toss value: ' + str(toss))
    logging.debug('Guess value: ' + str(guess))
    assert toss == 0 or toss == 1, 'toss doesn\'t contain a value of 0 or 1'
    assert guess == 0 or guess == 1, 'guess doesn\'t contain a value of 0 or 1'
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')


# Bugi:
#   1. statement toss == guess - nigdy nie zostanie spelniony(poprawione)(poprawione)
#   2. zla nazwa zmiennej 'guesss' zamiast 'guess'(poprawione)
#   3. brak walidacji guessa w drugim input()(poprawione)
