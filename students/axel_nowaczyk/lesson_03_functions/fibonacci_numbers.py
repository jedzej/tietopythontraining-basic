def fib(number):
    if number <= 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fib(number - 1) + fib(number - 2)


def program():
    number = int(input())
    print(fib(number))


if __name__ == '__main__':
    program()
