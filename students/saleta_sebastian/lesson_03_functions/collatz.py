def collatz(number):
    
    if number < 0:
        raise ValueError('Only positive numbers ')
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number +1


def main():

    try:
        collatz_number = collatz(int(input('Enter number: ')))
        while collatz_number != 1:
            collatz_number = collatz(collatz_number)
    except ValueError:
        print('You have input an int not a string')


if __name__ == '__main__':
    main()
