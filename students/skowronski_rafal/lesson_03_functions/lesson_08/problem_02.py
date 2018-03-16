# Solves 'Negative exponent' problem


def _power(a, n):
    return a ** n


def _main():
    a = float(input('Enter base (a) of the power function a\u207F: '))
    n = int(input('Enter exponent (n) of the power function a\u207F: '))

    power = _power(a, n)

    print('\na\u207F={0}'.format(power))


if __name__ == '__main__':
    _main()
