# https://snakify.org/lessons/functions/problems/fibonacci_rec/
# piotrsta


def fib(n):
    if n > 0:
        if int(n) == 2 or int(n) == 1:
            return 1
        else:
            return fib(int(n) - 1) + fib(int(n) - 2)
    else:
        print('Wrong value. You must enter a positive integer.')


if __name__ == '__main__':
    try:
        n = int(input('Enter integer value: '))
        print(fib(n))

    except ValueError:
        print('Wrong input value.')
