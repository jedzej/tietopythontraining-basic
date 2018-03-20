#!/usr/bin/env python3


def power(number, exponent):
    return number ** exponent


def main():
    number = float(input())
    exponent = int(input())
    print(power(number, exponent))


if __name__ == "__main__":
    main()
