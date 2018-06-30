def reverse():
    x = int(input())
    if x != 0:
        reverse()
    print(x)


def main():
    reverse()


if __name__ == '__main__':
    main()
