n = int(input())
sum_rem = 0
sum_all = 1

for i in range(2, n + 1):
    a = int(input())
    sum_rem += a
    sum_all += i

print(sum_all - sum_rem)
