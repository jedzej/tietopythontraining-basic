# https://automatetheboringstuff.com/chapter3/
# "The Collatz Sequence + Input Validation"
# piotrsta


def collatz(number):
    try:
        if int(number) <= 0:
            raise ValueError
        if int(number) % 2 == 0:
            value = int(number) // 2
            print(value)
        else:
            value = 3 * int(number) + 1
            print(value)
    except ValueError:
        print('Wrong value. You must enter a positive integer.')
        value = 1
    return value


number = input()
while number != 1:
    number = collatz(number)
