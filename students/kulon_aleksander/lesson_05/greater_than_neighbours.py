def func(arg):
    result = ''
    return result


def main():
    func(1)
    a = "-9 29 -100 64 26 73 -96 28 -92 11 -14 -86 -54 -67".split()
    a = input().split()
    for i in range(len(a)):
        if i > 0 and int(a[i]) > int(a[i - 1]):
            print(a[i] + ' ', end='')


if __name__ == '__main__':
    main()
