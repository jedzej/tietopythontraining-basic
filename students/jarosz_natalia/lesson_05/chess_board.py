def chess_board(n, m):
    a = []
    for i in range(n):
        a.append([])
        for j in range(m):
            if (i + j) % 2 == 0:
                a[i].append('.')
            else:
                a[i].append('*')
    for row in a:
        print(' '.join(row))


def main():
    n, m = [int(i) for i in input().split()]
    chess_board(n, m)


if __name__ == '__main__':
    main()
