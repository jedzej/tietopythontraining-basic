n = int(input())
sum_card = 0
sum2 = 0
for i in range(1, n):
    sum_card += int(input())
    sum2 += i
print(sum2 + n - sum_card)
