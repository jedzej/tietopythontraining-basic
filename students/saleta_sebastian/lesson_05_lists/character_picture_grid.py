def print_picture_grid(raw_grid):

    for i in range(len(raw_grid[0])):
        line = ''
        for j in range(len(raw_grid)):
            line += raw_grid[j][i]
        print(line)


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
    print_picture_grid(grid)


if __name__ == '__main__':
    main()
