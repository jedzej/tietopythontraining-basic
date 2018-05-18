# Given two positive integers m and n, m lines of n elements,
# giving an m×n matrix A, followed by two non-negative integers
# i and j less than n, swap columns i and j of A and print the result.
# Write a function swap_columns(a, i, j) and call it to exchange the columns.

def swap_columns(a, i, j):
    print(a)


def main():
    m, n = [int(s) for s in input().split()]
    A = []

    for row in range(m):
        A.append([int(col) for col in input().split()])

    print(A)

    i, j = [int(s) for s in input().split()]

    swap_columns(A, i, j)

    for k in A:
        print(' '.join(k))


if __name__ == "__main__":
    main()
