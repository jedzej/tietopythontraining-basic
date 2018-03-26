
def collatz(number):
    try:
        if number % 2 == 0:
            print(number // 2)
            return number // 2
        else:
            print(3 * number + 1)
            return 3 * number + 1
    except ValueError:
        print('Value rror')


if __name__ == "__main__":
    while True:
        try:
            integer = int(input('Integer: '))
            if integer < 0:
                raise ValueError
        except ValueError:
            print('Invalid integer')
        else:
            break

    x = collatz(integer)
    while x != 1:
        x = collatz(x)
