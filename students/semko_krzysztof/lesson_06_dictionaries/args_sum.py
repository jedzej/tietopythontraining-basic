"""
Args sum - write a function called sum_all
that takes any number of arguments and returns their sum.
"""


def sum_all(*args):
    return sum(args)


def main():
    print(sum_all(1, 2, 3, 4, 5))


if __name__ == '__main__':
    main()
