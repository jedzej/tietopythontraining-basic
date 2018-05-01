#!/usr/bin/env python3


def print_reversed():
    value = int(input())
    if value != 0:
        print_reversed()
    print(value)


if __name__ == "__main__":
    print_reversed()
