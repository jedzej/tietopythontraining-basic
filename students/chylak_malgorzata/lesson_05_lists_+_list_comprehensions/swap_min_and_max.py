a = [int(i) for i in input().split()]

minimum = 0
maximum = 0

for i in range(1, len(a)):
    if a[i] > a[maximum]:
        maximum = i
    if a[i] < a[minimum]:
        minimum = i

a[minimum], a[maximum] = a[maximum], a[minimum]

print(" ".join([str(i) for i in a]))
