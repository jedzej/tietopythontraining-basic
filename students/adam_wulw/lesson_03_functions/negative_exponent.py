def power(a, n):
    ret = 1
    if n > 0:
        for i in range(n):
            ret *= a
        return ret
    else:
        for i in range(-n):
            ret *= 1 / a
        return ret


a = float(input('Enter a\n'))
n = int(input('Enter n\n'))
print('Power {0} from {1} is {2}'.format(n, a, power(a, n)))
