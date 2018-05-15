def print_set(some_set):
    print(len(some_set))
    some_set.sort()
    for i in some_set:
        print(i)


def main():
    a = [int(i) for i in input().split()]
    n = []
    m = []

    result = []
    result_n = []
    result_m = []

    for i in range(a[0]):
        n.append(int(input()))
    for i in range(a[1]):
        m.append(int(input()))

    for i in n:
        if i in m:
            result.append(i)
        else:
            result_n.append(i)

    for i in m:
        if i not in result:
            result_m.append(i)

    print_set(result)
    print_set(result_n)
    print_set(result_m)


if __name__ == '__main__':
    main()
