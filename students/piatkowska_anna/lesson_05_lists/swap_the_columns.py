'''
Given two positive integers m and n, m
lines of n elements, giving an m×n matrix A,
followed by two non-negative integers i and j
less than n, swap columns i and j of A and print the result.
Write a function swap_columns(a, i, j) and call it to
exchange the columns.
'''


def swap_the_columns(a, i, j):
    for r in range(len(a)):
        matrix[r][i], matrix[r][j] = matrix[r][j], matrix[r][i]
    for r in range(len(a)):
        print(' '.join(matrix[r]))


if __name__ == "__main__":
    try:
        m, n = [int(s) for s in input("Enter matrix size [m n]:").split()]
        matrix = []
        for i in range(m):
            matrix.append(input("Enter row values:").split())
        swap_i, swap_j = [int(s) for s in input(
            "Enter index of columns that will be swap:").split()]
        swap_the_columns(matrix, swap_i, swap_j)
    except ValueError:
        print("Invalid input")
