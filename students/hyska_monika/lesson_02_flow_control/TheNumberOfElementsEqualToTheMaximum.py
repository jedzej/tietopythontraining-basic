# Program return number of elements equal to the maximum

n = int((input("put haw many elements want check:")))
N = []
i = 0

while i < n:
    print("Put", i + 1, "element:")
    l = int(input())
    N.append(l)
    i += 1

i = 0
max1 = 0

while i < len(N):
    if (N[i]) > max1:
        max1 = N[i]
    i += 1

c = N.count(max1)
print("maximum count:", c)
