# Solves problem 03 - Sum of digits
import math


def print_sum_of_digits():
    number = abs(int(input('Enter integer number: ')))

    sum = 0
    while number != 0:
        sum += number % 10
        number = number // 10

    print('\nSum of digits is: {0}'.format(sum))

if __name__ == '__main__':
    print_sum_of_digits()
