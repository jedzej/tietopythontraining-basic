number = int(input('Give the number of cards: '))

sum_cards = 0

for i in range(1, number + 1):
    sum_cards += i

for i in range(number - 1):
    sum_cards -= int(input())

print('{} {}'.format('Lost card is:', sum_cards))
