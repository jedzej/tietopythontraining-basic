n = int(input('n = '))

a = 1
result = 0

for i in range(n):
    a = a + (a * i)
    result += a

print(result)
