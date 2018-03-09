#!/usr/bin/env python3


def fib(number):
    if number < 2:
        return number
    return fib(number - 1) + fib(number - 2)


def main():
    number = int(input())
    print(fib(number))


if __name__== "__main__":
    main()
