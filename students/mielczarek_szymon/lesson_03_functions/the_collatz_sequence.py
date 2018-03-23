def collatz(number):
    if number < 0:
        raise ValueError('The number cannot be negative')
    if number % 2 == 0:
        ret = number // 2
    else:
        ret = 3 * number + 1
    print(ret)
    return ret


def main():
    try:
        number = int(input('Enter number: '))
    except ValueError:
        print('You must enter an integer!')
    else:
        while number > 1:
            number = collatz(number)


if __name__ == "__main__":
    main()
