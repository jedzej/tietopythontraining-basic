#!/usr/bin/env python3


from pprint import pprint


def inspect_object_attributes(obj):
    return {attr: getattr(obj, attr) for attr in dir(obj)}


def main():
    my_obj = 0.07
    pprint(inspect_object_attributes(my_obj))


if __name__ == "__main__":
    main()
