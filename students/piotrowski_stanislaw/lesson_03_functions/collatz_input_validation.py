# https://automatetheboringstuff.com/chapter3/
# "The Collatz Sequence + Input Validation"
# piotrsta


def collatz(argument):
    try:
        if argument <= 0:
            raise ValueError
        if argument % 2 == 0:
            value = argument // 2
        else:
            value = 3 * argument + 1
        return value

    except ValueError:
        print('Wrong value. You must enter a positive integer.')
        value = 1
    return value


if __name__ == '__main__':
    try:
        number = int(input())
        while number != 1:
            print(number)
            number = collatz(number)

    except ValueError:
        print('Wrong input value.')
