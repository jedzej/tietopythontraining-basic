a = int(input())
b = int(input())
n = int(input())

dollars = (a * n + b * n // 100)
cents = b * n % 100

print(dollars, cents)
