import random

guess = ''
choices = ('heads', 'tails')

while guess not in choices:
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

toss = choices[random.randint(0, 1)]  # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
