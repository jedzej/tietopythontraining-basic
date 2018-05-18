# Given two numbers n and m. Create a two-dimensional array of size (n×m)
# and populate it with the characters "." and "*" in a checkerboard pattern.
# The top left corner should have the character "." .

def main():
    n, m = [int(s) for s in input().split()]
    board = []

    for i in range(n):
        board.append(['.'] * m)

    for i in range(0, n):
        for j in range(0, m):
            if (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0):
                board[i][j] = '*'

    for k in board:
        print(' '.join(k))


if __name__ == "__main__":
    main()
