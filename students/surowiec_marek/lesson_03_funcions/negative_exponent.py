def power(a, n):
    if n == 0:
        return 1
    elif n > 0:
        return a * power(a, n - 1)
    else:
        n = 1 - n
        return 1 / power(a, n - 1)


number = float(input())
power_of_number = int(input())
print(power(number, power_of_number))
