#!/usr/bin/env python3
"""Sort decorator exercise"""
import random


def sort_decorator(original_function):
    """Decorator"""
    def wrapper():
        """Wrapper"""
        return sorted(original_function())
    return wrapper


@sort_decorator
def data_feeder():
    """Data feeder function"""
    return [4, 2, 1, 3]


@sort_decorator
def data_feeder_2():
    """Random data feeder function"""
    return random.sample(range(100), 10)


def main():
    """Main function"""
    print(data_feeder())
    print(data_feeder_2())


if __name__ == '__main__':
    main()
