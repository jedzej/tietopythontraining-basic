def collatz(number):
    collatzed_number = 0
    if number % 2 == 0:
        collatzed_number = number // 2
    else:
        collatzed_number = 3 * number + 1
    print(collatzed_number)
    return collatzed_number


def program():
    number = None
    while number is None:
        try:
            number = int(input())
        except ValueError:
            print("Number needs to be an integer")
    while number != 1:
        number = collatz(number)


if __name__ == '__main__':
    program()
