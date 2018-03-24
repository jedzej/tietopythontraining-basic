n = int(input())
sum_all_cards = n * (n + 1) // 2

for i in range(n - 1):
    sum_all_cards -= int(input())
print(sum_all_cards)
