a = 1
i = 0
tab = []
max = 0
max_cnt = 0

while a != 0:
    a = int(input("podaj liczbe: "))
    tab.append(a)
    i += 1
    if max < a:
        max = a
    if a == 0:
        break

for i in tab:
    if i == max:
        max_cnt += 1

print(max_cnt)
