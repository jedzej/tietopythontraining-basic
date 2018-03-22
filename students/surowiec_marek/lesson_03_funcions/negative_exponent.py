# Negative exponent
def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)


number = float(input())
power_of_number = int(input())
if power_of_number < 0:
    print(1 / power(number, - power_of_number))
else:
    print(power(number, power_of_number))
