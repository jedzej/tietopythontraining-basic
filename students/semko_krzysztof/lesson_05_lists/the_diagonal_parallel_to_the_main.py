"""
Given an integer n, produce a two-dimensional array
of size (n×n) and complete it according to the following
rules, and print with a single space between characters:

    On the main diagonal write 0 .
    On the diagonals adjacent to the main, write 1 .
    On the next adjacent diagonals write 2 and so forth.

Print the elements of the resulting array.
"""


def main():
    n = int(input())
    arr = [[0] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            else:
                arr[i][j] = abs(i - j)

    for row in arr:
        print(' '.join([str(elem) for elem in row]))


if __name__ == '__main__':
    main()
