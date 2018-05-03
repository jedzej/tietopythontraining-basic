"""
Given two numbers n and m. Create a two-dimensional
array of size (n×m) and populate it with the characters
"." and "*" in a checkerboard pattern.
The top left corner should have the character "." .
"""


def main():
    matrix = [int(x) for x in input().split()]

    rows, columns = matrix[0], matrix[1]

    for i in range(rows):
        line = []

        for j in range(columns):
            if (i + j) % 2 == 0:
                line.append('.')
            else:
                line.append('*')

        print(''.join(str(char) for char in line))


if __name__ == '__main__':
    main()
