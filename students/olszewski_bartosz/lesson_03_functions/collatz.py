def collatz(number):
    if number % 2 == 0:
        value = number // 2
    else:
        value = 3 * number + 1
    print(value)
    return value


try:
    a = int(input('Enter number: '))
    while a != 1:
        a = collatz(int(a))
except ValueError:
    print('Wrong argument, please give a number')
