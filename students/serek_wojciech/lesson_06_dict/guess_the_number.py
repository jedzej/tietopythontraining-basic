#!/usr/bin/env python3
"""Guess the number exercise"""


def main():
    """Main function"""
    n_value = int(input())
    numbers = set(range(1, n_value + 1))

    while True:
        user_guess = input()
        if user_guess == 'HELP':
            break
        response = input()
        if response == 'YES':
            numbers = numbers.intersection(set(user_guess.split()))
        elif response == 'NO':
            numbers = numbers.difference(set(user_guess.split()))

    print(' '.join(str(i) for i in list(numbers)))


if __name__ == '__main__':
    main()
