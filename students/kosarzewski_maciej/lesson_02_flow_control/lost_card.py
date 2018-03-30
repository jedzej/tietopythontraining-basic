number = int(input())
tmp = 0
a = 0
for i in range(2, number+1):
    numbers = int(input())
    tmp += numbers
for i in range(0, number+1):
    a += i
print(a-tmp)
