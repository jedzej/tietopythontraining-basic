n = int(input())
m = int(input())
d = m // n
if (m % n) > 0:
    d = d + 1
print(d)
