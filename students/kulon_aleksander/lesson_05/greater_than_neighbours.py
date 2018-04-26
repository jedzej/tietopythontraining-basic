def func():
    quantity = 0
    a = input().split()
    for i in range(1, len(a) - 1):
        if int(a[i - 1]) < int(a[i]) > int(a[i + 1]):
            quantity += 1
    print(quantity)


def main():
    func()


if __name__ == '__main__':
    main()
