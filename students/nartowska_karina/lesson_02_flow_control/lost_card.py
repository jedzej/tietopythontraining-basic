value = int(input())
tmp = 0
i = 0
total = value
for i in range(1, value):
    numbers = int(input())
    tmp += numbers
    total = total + i
print(total - tmp)
