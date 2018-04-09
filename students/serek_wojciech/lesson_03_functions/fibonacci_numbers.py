#!/usr/bin/env python3
"""Fibonacci numbers"""


def fib(value):
    """Fibonacci numbers"""
    if value == 1 or value == 2:
        return 1

    return fib(value - 1) + fib(value - 2)


def main():
    """Main function"""
    print(fib(int(input())))


if __name__ == '__main__':
    main()
