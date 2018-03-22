# Exponentiation
def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)

number = float(input())
power_of_number= int(input())
print(power(number, power_of_number))
