def fib(n):
    try:
        n = int(n)
        if n < 0:
            raise ValueError('Wrong Value')
        elif n == 1:
            return 1
        elif n == 0:
            return 0

        else:
            return fib(n - 1) + fib(n - 2)

    except ValueError:
        print('Wrong Value')
        exit()


if __name__ == "__main__":
    number = input("Positive integer: ")
    print(fib(number))
