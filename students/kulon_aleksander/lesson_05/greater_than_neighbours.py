def func():
    quantity = 0
    a = input().split()
    for i in range(len(a)):
        if i > 0 and int(a[i]) > int(a[i - 1]):
            quantity += 1
    print(quantity)


def main():
    func()


if __name__ == '__main__':
    main()
