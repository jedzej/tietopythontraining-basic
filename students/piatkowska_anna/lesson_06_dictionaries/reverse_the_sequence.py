'''
Statement
Given a sequence of integers that end with a 0.
Print the sequence in reverse order.
Don't use lists or other data structures.
Use the force of recursion instead.
'''


def get_int_and_print():
    a = int(input())
    if a != 0:
        get_int_and_print()
    print(a)


if __name__ == "__main__":
    print("Enter sequence of numbers, \
separated with new line character, end with 0:")
    get_int_and_print()
