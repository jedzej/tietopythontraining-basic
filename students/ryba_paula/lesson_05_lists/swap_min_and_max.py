def swap(a):
    minimum, maksimum = a.index(min(a)), a.index(max(a))
    a[maksimum], a[minimum] = a[minimum], a[maksimum]
    print(' '.join([str(i) for i in a]))


def main():
    a = [int(x) for x in input("Input list: ").split()]

    swap(a)


if __name__ == '__main__':
    main()
