def character_picture_grid(list_of_pixel):
    picture = ''
    for row in range(len(list_of_pixel[0])):
        for column in range(len(list_of_pixel)):
            picture += list_of_pixel[column][row]
        picture += '\n'
    return picture


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
    print(character_picture_grid(grid))


if __name__ == '__main__':
    main()
