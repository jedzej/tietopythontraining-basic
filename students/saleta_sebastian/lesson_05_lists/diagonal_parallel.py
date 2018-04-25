def diagonal_parallel(dimn):
    base_row = []
    for i in range(dimn):
        base_row.append([])
        for j in range(dimn):
            base_row[i].append(abs(i - j))
    print(base_row)

    matrix_in_str = ''
    for k in range(len(base_row)):
        matrix_in_str += ''.join(str(base_row[k])) + '\n'
    print(matrix_in_str)


def main():
    size = int(input())
    diagonal_parallel(size)


if __name__ == '__main__':
    main()
