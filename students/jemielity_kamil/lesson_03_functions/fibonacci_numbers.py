def fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n - 1) + fib(n - 2)


while True:
    number = int(input("Positive integer: "))
    try:
        if number < 0:
            raise ValueError
        else:
            print(fib(number))
            break
    except ValueError:
        print('Wrong value!\n')
