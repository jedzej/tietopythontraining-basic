#!/usr/bin/env python3


def reverse():
    try:
        number = int(input("Please enter integer number\n"))
    except ValueError:
        print("It was wrong number, try again\n")
        exit()

    if number is not 0:
        reverse()
    print(number)


def main():
    reverse()


if __name__ == "__main__":
    main()
