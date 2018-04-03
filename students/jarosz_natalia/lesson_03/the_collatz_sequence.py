def collatz(arg):
    if arg % 2 == 0:
        print(arg // 2)
        return arg // 2
    else:
        print(3 * arg + 1)
        return (3 * arg) + 1


def main():
    print("provide number")
    number = int(input())
    while number != 1:
        number = collatz(number)


if __name__ == "__main__":
    main()
