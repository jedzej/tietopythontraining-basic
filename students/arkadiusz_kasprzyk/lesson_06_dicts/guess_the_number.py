# guess_the_number.py

import random


def guess(N):

    prompt = "Give your guess (number between 1 " + \
             "and {} or one of '0', '?', 'h', 'help' for help):".format(N)
    guesset = input(prompt).split()
    if guesset[0].lower() in {'0', '?', 'h', 'help'}:
        geusset = set()
    else:
        guesset = set(guesset)
        geusset = set(map(int, guesset))
    return geusset


if __name__ == "__main__":

    N = int(input("Maximum number is: "))
    the_number = random.randint(1, N)
    possible = set(range(1, N + 1))
    while the_number in possible and len(possible) > 1:
        guesset = guess(N)
        if the_number in guesset:
            possible &= guesset
            print("YES")
        elif len(guesset) == 0:
            print("Numbers left: ")
            print(possible)
        else:
            possible -= guesset
            print("NO")
    print("You have guessed the number: {}.".format(the_number))
