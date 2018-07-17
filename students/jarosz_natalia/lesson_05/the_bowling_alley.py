def the_bowling():
    n, k = [int(s) for s in input().split()]
    bahn = ['I'] * n

    for i in range(k):
        left, right = [int(s) for s in input().split()]
        for j in range(left - 1, right):
            bahn[j] = '.'

    print(''.join(bahn))


def main():
    the_bowling()


if __name__ == '__main__':
    main()
