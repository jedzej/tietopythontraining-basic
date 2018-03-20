cards = int(input())

sum_of_cards = 0

for i in range(1, cards + 1):
    sum_of_cards += i

for i in range(cards - 1):
    sum_of_cards -= int(input())

print(sum_of_cards)
