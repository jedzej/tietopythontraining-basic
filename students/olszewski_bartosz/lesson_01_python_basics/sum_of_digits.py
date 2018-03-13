a = int(input('give a number '))
s = a // 100
a = a - s * 100
d = a // 10
a = a - d * 10
j = a // 1
print('sum of digits', d + s + j)
