#!/usr/bin/env python3


def fibonacci(n):
    if n < 0:
        raise ValueError
    if (n == 0) or (n == 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    try:
        number = int(input('Please enter non-negative integer number\n'))
        print(fibonacci(number))
    except ValueError:
        print('Not a valid number, try again')
        exit()


if __name__ == "__main__":
    main()
