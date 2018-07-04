#!/usr/bin/env python3


def print_rev_list():
    z = int(input())
    if z:
        print_rev_list()
    print(z)


if __name__ == "__main__":
    print_rev_list()
