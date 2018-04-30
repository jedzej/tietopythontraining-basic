def taking_input():
    n, k = [int(s) for s in input().split()]
    a = []
    for i in range(n):
        a.append([int(j) for j in input().split()])
    return a, n, k


def maximum_element(a, n, k):
    maxim = a[0][0]
    x, y = 0, 0
    for i in range(n):
        for j in range(k):
            if a[i][j] > maxim:
                maxim = a[i][j]
                x, y = i, j
    print(x, y)


matrix, row, column = taking_input()
maximum_element(matrix, row, column)
