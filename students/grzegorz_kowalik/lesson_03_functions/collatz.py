def collatz(number):
    print(number)

    if number == 1:
        return 1
    elif number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


if __name__ == '__main__':
    number = 1
    try:
        number = int(input())
    except ValueError:
        print("To nie liczba!")

    while number != 1:
        number = collatz(number)
