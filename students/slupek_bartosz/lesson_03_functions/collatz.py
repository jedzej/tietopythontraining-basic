def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1


if __name__ == '__main__':
    try:
        a = int(input('Enter number: '))
        while a > 1:
            collatz(int(a))
    except ValueError:
        print('Wrong argument, please give a number')
