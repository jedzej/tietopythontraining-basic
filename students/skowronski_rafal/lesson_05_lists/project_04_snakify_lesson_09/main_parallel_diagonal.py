from helper import print_matrix_as_string


def get_matrix(matrix_size):
    return [[abs(col - row) for col in range(matrix_size)]
            for row in range(matrix_size)]


if __name__ == '__main__':
    matrix_size = int(input('Enter matrix size: '))

    matrix = get_matrix(matrix_size)

    print_matrix_as_string(matrix)
