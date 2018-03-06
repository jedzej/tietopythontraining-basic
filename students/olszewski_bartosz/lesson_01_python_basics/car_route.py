from math import ceil
a = int(input('set number of kilometers'))
print('set car kilometers capacity per day')
b = int(input())
x = b / a
y = ceil(x)
print('distance covered by car in', y, 'days')
