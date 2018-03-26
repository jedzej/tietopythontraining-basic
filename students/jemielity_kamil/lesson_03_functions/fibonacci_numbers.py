def fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    elif n < 0:
        raise ValueError('Wrong value')
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    number = int(input("Positive integer: "))
    print(fib(number))
