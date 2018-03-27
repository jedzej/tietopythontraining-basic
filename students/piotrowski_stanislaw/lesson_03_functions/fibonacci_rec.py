# https://snakify.org/lessons/functions/problems/fibonacci_rec/
# piotrsta


def fib(n):
    if int(n) == 2 or int(n) == 1:
        return 1
    else:
        return fib(int(n) - 1) + fib(int(n) - 2)


def is_positive_int(value):
    try:
        if int(value) > 0:
            return True
    except ValueError:
        return False


n = input('Enter integer value: ')

if is_positive_int(n):
    print(fib(n))
else:
    print('Wrong input value.')
