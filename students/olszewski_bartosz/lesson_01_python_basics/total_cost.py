a = int(input())
b = int(input())
n = int(input())
cents = a * 100 + b
cost = n * cents
print('Cost {}.{}$'.format(cost // 100, cost % 100))
