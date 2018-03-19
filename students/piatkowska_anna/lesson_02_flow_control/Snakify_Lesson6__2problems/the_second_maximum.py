# Statement
# The sequence consists of distinct positive integer numbers
# and ends with the number 0.
# Determine the value of the second largest element in this sequence.
# It is guaranteed that the sequence has at least two elements.


def second_maximum():
    second = 0
    print("Enter positive integer number:")
    first = int(input())
    a = first
    while(a != 0):
        print("Enter a positive integer number (0 to end processing)):")
        a = int(input())
        if (a > first):
            first, second = a, first
        elif (a > second):
            second = a
    print("The second maximum value is:")
    print(second)


if __name__ == '__main__':
    second_maximum()
