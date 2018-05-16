# Program return what number is missing

n = int((input("put haw many elements want check:")))
N = []

for i in range(1, n + 1):
    print("Put", i + 1, "element:")
    l = int(input())
    N.append(l)

N.sort()
miss = N[-1]

for i in range(1, n + 1):
    if N[i - 1] != i:
        miss = i
        break

print("missing:", miss)
