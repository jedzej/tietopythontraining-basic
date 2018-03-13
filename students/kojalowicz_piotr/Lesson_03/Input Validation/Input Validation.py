def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


def collatz_loop():
    number = int(input())
    while number != 1:
        number = collatz(number)
        print(number)


try:
    collatz_loop()
except ValueError:
    print('must enter an integer')

