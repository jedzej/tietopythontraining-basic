#!/usr/bin/env python3

def print_sum_of_three_numbers():
    number_1 = float(input('Enter first number: '))
    number_2 = float(input('Enter second number: '))
    number_3 = float(input('Enter third number: '))
    
    sum = number_1 + number_2 + number_3

    print('Sum: ', sum)



if __name__ == '__main__':
    print_sum_of_three_numbers()