# https://automatetheboringstuff.com/chapter3/
# "The Collatz Sequence + Input Validation"
# piotrsta


def collatz(argument):
    if int(argument) % 2 == 0:
        value = int(argument) // 2
    else:
        value = 3 * int(argument) + 1
    return value


def is_positive_int(value):
    try:
        if int(value) > 0:
            return True
    except ValueError:
        return False


if __name__ == '__main__':
    number = input()
    if is_positive_int(number):
        while number != 1:
            number = collatz(number)
            print(number)
    else:
        print('Wrong value. You must enter a positive integer.')
