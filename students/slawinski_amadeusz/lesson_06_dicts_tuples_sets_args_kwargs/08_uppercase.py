#!/usr/bin/env python3


def capitalize(string):
    return string[0].upper() + string[1:]


if __name__ == "__main__":
    readline = input()
    capline = [capitalize(word) for word in readline.split()]
    print(' '.join(capline))
