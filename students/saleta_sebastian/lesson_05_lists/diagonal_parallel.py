def diagonal_parallel(dimn):
    base_row = []
    for i in range(dimn):
        base_row.append([])
        for j in range(dimn):
            base_row[i].append(abs(i - j))


    matrix_in_str = ''
    for k in base_row:
        print(' '.join([str(i) for i in k]))


def main():
    size = int(input())
    diagonal_parallel(size)


if __name__ == '__main__':
    main()
