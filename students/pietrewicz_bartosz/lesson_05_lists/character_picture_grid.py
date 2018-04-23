

# Prints rectangular image, assumes that all elements of the list passed as parameter
# are lists of the same length
def print_image(image):
    width = len(image)
    height = len(image[0])
    for y in range(height):
        for x in range(width):
            print(image[x][y], end='')
        print()


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
    print_image(grid)


if __name__ == '__main__':
    main()
