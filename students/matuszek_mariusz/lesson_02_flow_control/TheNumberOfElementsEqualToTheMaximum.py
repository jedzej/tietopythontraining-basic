l = []
k = 0
count = 0

while True:
    n = int(input('n' + str(k + 1) + ' = '))
    k += 1

    if n == 0:
        break
    else:
        l.append(n)

for i in range(len(l)):
    if max(l) == l[i]:
        count += 1

print(count)
