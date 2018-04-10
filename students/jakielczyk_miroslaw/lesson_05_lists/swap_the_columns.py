def swap_columns(array, i, j):
    for element in array:
        element[i], element[j] = element[j], element[i]
    return array


def main():
    size = input()
    m = int(size.split(' ')[0])
    array = []
    for y in range(int(m)):
        row = input().split(' ')
        array.append(row)
    row_column = input()
    i = int(row_column.split(' ')[0])
    j = int(row_column.split(' ')[1])
    array_after_swap = swap_columns(array, i, j)
    for element in array_after_swap:
        print(' '.join(element))


if __name__ == "__main__":
    main()
