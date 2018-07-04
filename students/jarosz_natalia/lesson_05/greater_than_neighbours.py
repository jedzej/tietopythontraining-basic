def greater_than():
    count = 0
    x = input().split()
    for i in range(1, len(x) - 1):
        if int(x[i - 1]) < int(x[i]) > int(x[i + 1]):
            count += 1
    print(count)


def main():
    greater_than()


if __name__ == '__main__':
    main()
