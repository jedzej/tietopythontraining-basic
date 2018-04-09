# Project: The Collatz Sequence


def collatz(number):
    if number % 2 == 0:
        ret_number = number // 2
    else:
        ret_number = 3 * number + 1

    return ret_number


def _main():
    number = int(input('Please enter an integer number: '))

    while True:
        number = collatz(number)
        print(number)
        if number == 1:
            break


if __name__ == '__main__':
    _main()
