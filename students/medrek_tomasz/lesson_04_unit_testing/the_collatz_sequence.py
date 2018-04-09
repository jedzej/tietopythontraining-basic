#!/usr/bin/env python3


def collatz(input_number):
    if (input_number % 2):
        return 3 * input_number + 1
    else:
        return input_number // 2


def main():
    try:
        number = int(input("Please enter a number:\n"))
        if (number < 2):
            raise ValueError
    except ValueError:
        print('That was not integer number greater than 1, please try again')
        exit()

    while (number != 1):
        number = collatz(number)
        print(number)


if __name__ == "__main__":
    main()
