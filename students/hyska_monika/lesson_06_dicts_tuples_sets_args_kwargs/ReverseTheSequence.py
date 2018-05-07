# Given a sequence of integers that end with a 0.
# Print the sequence in reverse order.
# Don't use lists or other data structures.


def int_revers():
    n = int((input("Put number:")))
    if n == 0:
        print(n)
        return n
    else:
        int_revers()
        print(n)
        return n


int_revers()
