import random


def main():
    guess = ''
    while guess not in ('heads', 'tails'):
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()
    toss = random.randint(0, 1)
    toss = ['heads', 'tails'][toss]
    if toss == guess:
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guess = input()
        if toss == guess:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')


if __name__ == "__main__":
    main()
