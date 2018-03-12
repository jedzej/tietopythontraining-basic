n = int(input())

sum = 0
sum_of_cards = 0

for i in range(1, n + 1):
    sum += i
for j in range(1, n):
    k = int(input())
    sum_of_cards += k

print(sum - sum_of_cards)
