def main():
    n = int(input())
    matrix = [[abs(x - y) for y in range(n)] for x in range(n)]
    for row in matrix:
        for column in row:
            print(column, end=" ")
        print()


if __name__ == '__main__':
    main()
