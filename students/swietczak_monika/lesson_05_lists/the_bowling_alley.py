alley = ""
n, k = [int(s) for s in
        input("Enter number of pins and number of balls: ").split()]

for i in range(n):
    alley += "I"

list_alley = list(alley)

if k > 0:
    for i in range(k):
        a = [int(s) for s in
             input("Enter range of knocked down pins: ").split()]
        # print(a)
        for j in range(a[0] - 1, a[1]):
            list_alley[j] = "."

print(''.join(list_alley))
