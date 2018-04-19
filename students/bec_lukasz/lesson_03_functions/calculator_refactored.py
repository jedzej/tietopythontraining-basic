def adding(first, second):
    return int(first) + int(second)


def subtract(first, second):
    return int(first) - int(second)


def multiply(first, second):
    return int(first) * int(second)


def divide(first, second):
    try:
        return int(first) / int(second)
    except ZeroDivisionError:
        print('Cannot divide by zero')


def power(first, second):
    return int(first)**int(second)


while True:
    firstNumber = input('Enter first number or \'q\' to quit: ')
    if firstNumber == 'q':
        break
    operationType = input('Enter one of operands + - * / ** or \'q\' to quit')
    if operationType == 'q':
        break
    secondNumber = input('Second Number or \'q\': ')
    if str(secondNumber) == 'q':
        print('opp type')
        break
    if operationType == '+':
        print(adding(firstNumber, secondNumber))
    if operationType == '-':
        print(subtract(firstNumber, secondNumber))
    if operationType == '*':
        print(multiply(firstNumber, secondNumber))
    if operationType == '/':
        print(divide(firstNumber, secondNumber))
    if operationType == '**':
        print(power(firstNumber, secondNumber))
