import random
guess = ''
heads = '1'
tails = '0'

while guess not in (heads, tails):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    toss = random.randint(0, 1) # 0 is tails, 1 is heads
    if str(toss) == guess:
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guess = input()
        if str(toss) == guess:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')