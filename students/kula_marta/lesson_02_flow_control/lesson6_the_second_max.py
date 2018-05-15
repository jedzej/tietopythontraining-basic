a = 1
i = 0
tab = []

while a != 0:
    a = int(input("podaj liczbe: "))
    tab.append(a)
    i += 1
    if a == 0:
        break
tab.sort()
print(len(tab))
print(tab)

print(tab[len(tab) - 2])
