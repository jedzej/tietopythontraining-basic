N = int(input())

i_list = []

for x in range(N):
    i_list.append(int(input()))

res = 0
for y in i_list:
    if y == 0:
        res += 1

print(res)
