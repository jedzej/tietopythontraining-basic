def print_array(n):
    array = []

    for i in range(n):
        array.append([])
        for j in range(n):
            array[i].append(abs(i - j))

    for row in array:
        print(' '.join([str(i) for i in row]))


def main():
    n = int(input("Input the size of the two-dimensional array (n×n): "))
    print_array(n)


if __name__ == '__main__':
    main()
