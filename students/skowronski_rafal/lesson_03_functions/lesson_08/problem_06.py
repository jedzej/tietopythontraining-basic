# Solves 'Fibonacci numbers' problem


def _fib(n):
    if n == 1 or n == 2:
        return 1
    return _fib(n - 1) + _fib(n - 2)


def _main():
    n = int(input(
        'Enter nth number of the Fibonacci sequence (non-negative integer): '))

    fibonacci_number = _fib(n)

    print('\nnth Fibonacci number: {0}'.format(fibonacci_number))


if __name__ == '__main__':
    _main()
