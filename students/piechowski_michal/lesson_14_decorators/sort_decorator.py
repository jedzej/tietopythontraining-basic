#!/usr/bin/env python3


def sort(func):

    def func_wrapper():
        return sorted(func())
    return func_wrapper


@sort
def data_feeder():
    return [4, 2, 1, 3]


def main():
    print("This is how data looks like: " + str(data_feeder()))
    print("Is data sorted? -> " + str(data_feeder() == [1,2,3,4]))


if __name__ == "__main__":
    main()
