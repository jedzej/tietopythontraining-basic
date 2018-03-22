def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


def input_collatz():
    print("Type an positive integer: ")
    number = int(input())
    while number != 1:
        number = collatz(number)
        print(number)


def main():
    try:
        input_collatz()
    except ValueError:
        print("Value must be an integer")


if __name__ == "__main__":
    main()
