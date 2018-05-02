#!/usr/bin/env python3


import pprint


def inspect_args(*args, **kwargs):
    pp = pprint.PrettyPrinter(width=1)
    print("Passed args:")
    pp.pprint(args)

    print("Passed kwargs:")
    pp.pprint(kwargs)


def main():
    inspect_args(1, 2, 'a', 'b', [1, 2], ['a', 'b'], range(1, 2), {1, 2},
                 dict(zip(['k', 'l'], range(1, 3))), a=1, b=2, c={1, 2},
                 d=dict(x=1, y=2))


if __name__ == "__main__":
    main()
