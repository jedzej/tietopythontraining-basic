"""
Given a sequence of integers that end with a 0.
Print the sequence in reverse order.

Don't use lists or other data structures.
Use the force of recursion instead.
"""
# note: This works in python 3.6!


def read_input(*args):
    t = int(input())
    if t != 0:
        print(str(args))
        read_input(*args, t)
    else:
        print(t)
        reverse(*args)
        return


def reverse(*args):
    if len(args) == 0:
        return

    print(args[-1])
    reverse(*args[:-1])


def main():
    read_input()


if __name__ == '__main__':
    main()
