digit = int(input())
h = digit // 100
d = (digit % 100 - digit % 10)//10
s = digit % 10

print(h+d+s)