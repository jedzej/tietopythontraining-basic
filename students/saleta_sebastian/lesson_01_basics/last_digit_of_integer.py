def last_digit_of_integer(number):
    lastdigit = number % 10
    print ('last digit of number {} is {}'.format(number, lastdigit))

if __name__ == '__main__':
    number = int(input())
    last_digit_of_integer(number)
