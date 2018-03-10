from math import ceil

a = int(input("First classroom: "))
b = int(input("Second classroom: "))
c = int(input("Third classroom: "))

a = ceil(a/2)
b = ceil(b/2)
c = ceil(c/2)

print(a+b+c)
