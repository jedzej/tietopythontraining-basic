#!/usr/bin/env python3

"""
sort.py: a practice project number 1 from:
Lesson 14 - Decorators

"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


def sort(fun):
    """
    This function is a  decorator that when applied to a function that returns
    a list, sorts this list
    :param fun: reference to a function object with return type list
    """
    def wrapper():
        return sorted(fun())
    return wrapper


@sort
def data_feeder():
    return [4, 2, 1, 3]


def main():
    print(data_feeder() == [1, 2, 3, 4])


if __name__ == '__main__':
    main()
