def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


def main():
    print('Enter number')
    number = 0

    while 1:
        number = int(input())
        if collatz(number) != 1:
            print(collatz(number))
        else:
            break


if __name__ == "__main__":
    main()
