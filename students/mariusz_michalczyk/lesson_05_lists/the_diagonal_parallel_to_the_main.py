def generate_array(dimension):
    two_dim_array = []
    for index in range(dimension):
        down = [i for i in range(index, 0, -1)]
        up = [i for i in range(0, dimension - index, 1)]
        two_dim_array.append(down + up)
    return two_dim_array


def show_array(two_dim_array):
    for row in two_dim_array:
        for value in row:
            print(str(value), end=" ")
        print('', end='\n')


if __name__ == '__main__':
    dimension = int(input())
    two_dim_array = generate_array(dimension)
    show_array(two_dim_array)
