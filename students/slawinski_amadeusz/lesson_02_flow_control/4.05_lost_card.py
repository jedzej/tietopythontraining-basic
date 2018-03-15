# find missing card number in set of cards

cards = int(input())

missing_card = int(cards * (cards + 1) / 2)

for c in range(1, cards):
    missing_card -= int(input())

print(missing_card)
