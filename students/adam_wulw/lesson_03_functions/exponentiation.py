def power(a, n):
    if n > 0:
        return a * power(a, n - 1)
    else:
        return 1


a = int(input('Enter a\n'))
n = int(input('Enter n\n'))
print('Power {0} from {1} is {2}'.format(n, a, power(a, n)))
