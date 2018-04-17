def produce_array(n):
    a = []

    for i in range(n):
        a.append([])
        for j in range(n):
            a[i].append(abs(i - j))

    for row in a:
        print(' '.join([str(i) for i in row]))


def main():
    n = int(input("Input the size: "))

    produce_array(n)


if __name__ == '__main__':
    main()
