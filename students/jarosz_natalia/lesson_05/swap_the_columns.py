def swap_columns(a, i, j):
    for y in range(len(a)):
            a[y][i], a[y][j] = a[y][j], a[y][i]

    for y in range(len(a)):
        for x in range(len(a[0])):
            print(str(a[y][x]) + ' ', end='')
        print('')


def main():
    n, m = [int(i) for i in input().split()]
    a = [[int(j) for j in input().split()] for i in range(n)]
    i, j = [int(i) for i in input().split()]

    swap_columns(a, i, j)


if __name__ == '__main__':
    main()
