#!/usr/bin/env python3


def sum_all(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum


def main():
    print(sum_all(4, 6, 2, 7))


if __name__ == "__main__":
    main()
