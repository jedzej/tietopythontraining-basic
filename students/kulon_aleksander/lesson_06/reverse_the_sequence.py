def func():
    a = int(input())
    if a != 0:
        func()
    print(a)


def main():
    func()


if __name__ == '__main__':
    main()
