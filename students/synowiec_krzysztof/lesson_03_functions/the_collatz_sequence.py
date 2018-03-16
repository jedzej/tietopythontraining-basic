def main():
    number = get_initial_number()
    while True:
        result = collatz(number)
        if result != 1:
            number = result
        else:
            break


def get_initial_number():
    while True:
        try:
            number = int(input('Please provide number\n'))
            return number
        except ValueError:
            print("You must provide integer. Try again!")


def collatz(number):
    if number % 2 == 0:
        result = (number // 2)
    else:
        result = 3 * number + 1
    print(result)
    return result


if __name__ == '__main__':
    main()
