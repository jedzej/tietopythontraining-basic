def get_array_based_on_user_input():
    two_dim_array = []
    n, m = [int(s) for s in input().split()]
    for i in range(n):
        row = [int(s) for s in input().split()]
        two_dim_array.append(row)
    return two_dim_array


def find_index_of_max_value(two_dim_array):
    max_index_row, max_index_column = 0, 0
    for index_row, row in enumerate(two_dim_array):
        for index_column, value in enumerate(row):
            if value > two_dim_array[max_index_row][max_index_column]:
                max_index_row, max_index_column = index_row, index_column
    return max_index_row, max_index_column


if __name__ == '__main__':
    max_index_row, max_index_column = find_index_of_max_value(get_array_based_on_user_input())
    print(max_index_row, max_index_column)
