import random


def guess():
    guess = ''
    while guess not in ('heads', 'tails'):
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()

    if guess == 'heads':
        return 1
    else:
        return 0


toss = random.randint(0, 1)   # 0 is tails, 1 is heads
print(toss)
guesses = guess()
if toss == guesses:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesses = guess()
    if toss == guesses:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
