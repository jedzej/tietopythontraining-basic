# Solves 'Exponentiation' problem


def _power(a, n):
    return 1 if n == 0 else a * _power(a, n - 1)


def _main():
    a = float(input('Enter positive base (a) of the power function a\u207F: '))
    n = int(input(
            'Enter non-negative exponent (n) of the power function a\u207F: '))

    power = _power(a, n)

    print('\na\u207F={:.3f}'.format(power))


if __name__ == '__main__':
    _main()
