#!/usr/bin/env python3


def nice_print(things):
    if not things:
        pass
    elif len(things) == 1:
        print(things[0])
    else:
        print(', '.join(things[0:-1]) + ' and ' + things[-1])


if __name__ == '__main__':
    spam = ['apples', 'bananas', 'tofu', 'cats']
    nice_print(spam)
    spam = ['apples', 'bananas', 'tofu']
    nice_print(spam)
    spam = ['apples', 'bananas']
    nice_print(spam)
    spam = ['apples']
    nice_print(spam)
    spam = []
    nice_print(spam)
