

def swap_columns(a, i, j):
    if i != j:
        for k in range(len(a)):
            a[k][i], a[k][j] = a[k][j], a[k][i]


def main():
    rows, columns = [int(x) for x in input().split()]
    a = []
    for i in range(rows):
        a.append([x for x in input().split()])
    c1, c2 = [int(x) for x in input().split()]

    swap_columns(a, c1, c2)

    for i in range(rows):
        print(' '.join(a[i]))


if __name__ == '__main__':

    main()
