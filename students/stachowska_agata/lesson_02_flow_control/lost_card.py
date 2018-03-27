N = int(input())
sum_of_cards = 0
for i in range(1, N + 1):
    sum_of_cards += i

for i in range(1, N):
    card = int(input())
    sum_of_cards -= card

print(sum_of_cards)
