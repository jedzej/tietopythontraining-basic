#!/usr/bin/env python3


def transpose_matrix_and_ret_str(matrix):
    output_string = ''

    if not isinstance(matrix[0], list):
        for element in matrix:
            output_string += element + '\n'
    else:
        # complementing missing matrix elements if needed
        num_of_cols = 0
        for row in matrix:
            num_of_cols = max(num_of_cols, len(row))
        for row in matrix:
            while len(row) < num_of_cols:
                row.append('')

        # transpositioning
        transposed_matrix = zip(*matrix)

        # converting to single string
        for row in transposed_matrix:
            output_string += ''.join(row) + '\n'

    return output_string[:-1]


def main():
    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]

    print(transpose_matrix_and_ret_str(grid))


if __name__ == "__main__":
    main()
