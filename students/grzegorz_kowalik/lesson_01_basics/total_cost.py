a = int(input())
b = int(input())
n = int(input())

c = a * 100 + b
c = c * n

a = c // 100
b = c % 100

print(str(a) + " " + str(b))