'''
Given an integer n, produce a two-dimensional array of size (n×n)
and complete it according to the following rules,
and print with a single space between characters:
On the main diagonal write 0 .
On the diagonals adjacent to the main, write 1.
On the next adjacent diagonals write 2 and so forth.
Print the elements of the resulting array.
'''


def create_matrix(n):
    matrix = [0] * n
    matrix = [[abs(j - i) for j in range(n)] for i in range(n)]
    for row in matrix:
        print(' '.join([str(elem) for elem in row]))


if __name__ == "__main__":
    try:
        n = int(input("Enter number that specifies size of the matrix: "))
        create_matrix(n)
    except ValueError:
        print("Invalid input")
