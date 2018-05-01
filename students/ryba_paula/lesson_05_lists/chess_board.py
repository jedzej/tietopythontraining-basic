def chess_board(rows, columns):
    a = []
    for i in range(rows):
        a.append([])
        for j in range(columns):
            if (i + j) % 2 == 0:
                a[i].append('.')
            else:
                a[i].append('*')

    for row in a:
        print(' '.join(row))


def main():
    rows, columns = [int(i) for i in input("Input rows and columns: ").split()]
    chess_board(rows, columns)


if __name__ == '__main__':
    main()
