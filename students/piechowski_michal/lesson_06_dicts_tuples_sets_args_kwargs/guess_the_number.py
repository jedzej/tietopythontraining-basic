#!/usr/bin/env python3


def main():
    n = int(input())
    yes_set = set()
    no_set = set()

    for i in range(0, n):
        alice_sentence = input()
        if alice_sentence == "HELP":
            break
        guess = set(alice_sentence.split())

        bob_sentence = input()
        if bob_sentence == "YES":
            if yes_set:
                yes_set = yes_set.intersection(guess)
            else:
                yes_set = guess
        else:
            no_set.update(guess)

    if yes_set:
        for element in sorted(yes_set.difference(no_set)):
            print(element, end=" ")
    else:
        for i in range(1, n + 1):
            if i not in no_set:
                print(i, end=" ")


if __name__ == "__main__":
    main()
