# https://automatetheboringstuff.com/chapter3/
# "The Collatz Sequence"
# piotrsta


def collatz(argument):
    if int(argument) % 2 == 0:
        value = int(argument) // 2
    else:
        value = 3 * int(argument) + 1
    return value


number = input()
while number != 1:
    number = collatz(number)
    print(number)
