#!/usr/bin/env python3


def power(number, expontent):
    if expontent == 0:
        return 1
    return number * power(number, expontent - 1)


def main():
    number = float(input())
    exponent = int(input())
    print(power(number, exponent))


if __name__== "__main__":
    main()
