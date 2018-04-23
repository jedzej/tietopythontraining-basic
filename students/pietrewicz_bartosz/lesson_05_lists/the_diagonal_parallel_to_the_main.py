

def main():
    n = int(input())
    a = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(abs(j - i))
        a.append(row)

    for i in range(n):
        for j in range(n - 1):
            print(str(a[i][j]) + ' ', end='')
        print(a[i][n - 1])


if __name__ == '__main__':
    main()
