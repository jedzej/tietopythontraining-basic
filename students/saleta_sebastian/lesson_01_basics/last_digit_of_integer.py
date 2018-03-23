def last_digit_of_integer():
    number = int(input())
    lastdigit = number % 10
    print ('last digit of number {} is {}'.format(number, lastdigit))


if __name__ == '__main__':
    last_digit_of_integer()
