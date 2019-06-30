import random


coin = {'tails': 0, 'heads': 1}


def guesss():
    guess = ''
    while guess not in ('heads', 'tails'):
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()
    return guess


toss = random.randint(0, 1)  # 0 is tails, 1 is heads
print(toss)
if toss == coin[guesss()]:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    if toss == coin[guesss()]:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
