#!/usr/bin/env python3


def sort_decorator(func):
    def func_wrapper():
        return sorted(func())
    return func_wrapper


@sort_decorator
def data_feeder():
    return [4, 2, 1, 3]


def main():
    print(data_feeder())


if __name__ == "__main__":
    main()
