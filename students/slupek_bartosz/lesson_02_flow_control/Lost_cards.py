n = int(input())
sum_cards = 0
for i in range(1, n + 1):
    sum_cards += i
for i in range(n - 1):
    sum_cards -= int(input())
print(sum_cards)
