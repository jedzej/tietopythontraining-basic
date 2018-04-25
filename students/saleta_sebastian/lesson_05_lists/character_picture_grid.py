def get_picture_grid(raw_grid):
    picture_grid = ''
    transposed_matrix = zip(*raw_grid)

    for i in range(len(transposed_matrix)):
        picture_grid += ''.join(transposed_matrix[i]) + '\n'

    return picture_grid


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
    transpose_matrix = get_picture_grid(grid)
    print(transpose_matrix)


if __name__ == '__main__':
    main()
