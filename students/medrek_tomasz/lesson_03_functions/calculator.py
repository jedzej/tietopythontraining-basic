#!/usr/bin/env python3


def calculate(a, b, option):
    if option == 'a':
        return a + b
    elif option == 's':
        return a - b
    elif option == 'm':
        return a * b
    elif option == 'd':
        return a / b
    elif option == 'e':
        return a ** b


def help():
    print('a - add\n'
          's - subtract\n'
          'm - multiply\n'
          'd - divide\n'
          'e - exponentiate\n'
          'q - QUIT')


options = ['a', 's', 'm', 'd', 'e', 'q']

print('Welcome to calculator:')
help()

while True:
    option = input('Please enter an option\n')
    if option not in options:
        print('Try again with possible option!\n')
        help()
        continue

    if option == 'q':
        print('GOOD BYE')
        break

    try:
        x = float(input('Please enter first operand\n'))
        y = float(input('Please enter second operand\n'))
    except ValueError:
        print('Not a valid number, please try again\n')
        continue

    try:
        print('Result is:\n{}\n'.format(calculate(x, y, option)))
    except Exception as e:
        print('Calculation failed because of: {}\n'.format(e))
