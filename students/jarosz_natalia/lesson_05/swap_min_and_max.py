def func():
    a = [int(s) for s in input().split()]
    index_of_min = 0
    index_of_max = 0

    for i in range(1, len(a)):
        if a[i] > a[index_of_max]:
            index_of_max = i
        if a[i] < a[index_of_min]:
            index_of_min = i
    a[index_of_min], a[index_of_max] = a[index_of_max], a[index_of_min]

    print(' '.join([str(i) for i in a]))


def main():
    func()


if __name__ == '__main__':
    main()
