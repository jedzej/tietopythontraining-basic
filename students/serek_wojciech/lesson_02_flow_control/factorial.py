#!/usr/bin/env python3
"""Factorial"""


def main():
    """Main function"""
    number = int(input())

    fact = 1
    for i in range(1, number + 1):
        fact = fact * i

    print(fact)


if __name__ == '__main__':
    main()
