# Solves problem 11 - chocolate bar


def _main():
    n = int(input('Enter length of the first side of the chocolate (n)): '))
    m = int(input('Enter length of the second side of the chocolate (m)): '))
    k = int(input('Enter number of squares (k): '))

    is_split_possible = (k / n < m and k % n == 0) or \
        (k / m < n and k % m == 0)

    print('{0}'.format('YES' if is_split_possible is True else 'NO'))


if __name__ == '__main__':
    _main()
