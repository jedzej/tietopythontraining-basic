def collatz(number):
    if number <= 0:
        raise ValueError
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


def validate_input():
    number = int(input("Type an integer: "))
    while number != 1:
        number = collatz(number)
        print(number)


def main():
    while True:
        try:
            validate_input()
            break
        except ValueError:
            print("Wrong input parameter. Try again.")
            continue


if __name__ == '__main__':
    main()
