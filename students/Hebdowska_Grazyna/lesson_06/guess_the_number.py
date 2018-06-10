import random


def guess_the_number(guess, number):
    if number in guess:
        return "YES"
    else:
        return "NO"


data = int(input())
number = str(random.randint(0, data))
guess = []

while "HELP" not in guess:
    guess = input().split(' ')
    if "HELP" in guess:
        break
    print(guess_the_number(guess, number))


if "help" in guess:
    print("help")
