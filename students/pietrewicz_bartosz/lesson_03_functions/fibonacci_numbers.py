def fib(n):
    """Returns n'th number in the Fibonacci sequence"""
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def main():
    # read integer n
    n = int(input())
    # print the n'th fibonacci number
    print(fib(n))


if __name__ == '__main__':
    main()
