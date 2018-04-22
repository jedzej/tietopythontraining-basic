
def diagonal_parallel_to_the_main():

    n = int(input())
    array = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        counter = 1
        for j in range(i + 1, n):
            array[i][j] = counter
            counter += 1

    for i in range(n):
        counter = 1
        for j in range(i + 1, n):
            array[j][i] = counter
            counter += 1

    for row in array:
        print(' '.join([str(elem) for elem in row]))


if __name__ == '__main__':
    diagonal_parallel_to_the_main()
