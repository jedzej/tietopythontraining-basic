#!/usr/bin/env python3


def collatz(number):
    if number < 1:
        raise ValueError("Number has to be >= 1")

    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1


def main():
    try:
        number = int(input("Give number for collatz function: "))
    except ValueError:
        print("You must input an integer!")
        quit()

    while True:
        number = collatz(number)
        if number == 1:
            break


if __name__ == "__main__":
    main()
