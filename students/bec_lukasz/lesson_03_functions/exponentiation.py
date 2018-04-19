def power(a, n):
    return a * pow(a, n - 1)


first = float(input('Enter a:'))
second = int(input('Enter n:'))

print(power(first, second))
