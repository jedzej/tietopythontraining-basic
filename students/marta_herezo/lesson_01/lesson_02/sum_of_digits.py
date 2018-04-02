a = int(input())

a1 = a % 10
a2 = a // 10
a3 = a2 % 10
a4 = a // 100

print(a1)
print(a3)
print(a4)
print('sum of three digits ' + str(a1 + a3 + a4))
