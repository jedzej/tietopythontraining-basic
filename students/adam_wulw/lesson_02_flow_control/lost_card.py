num = int(input('Enter number of cards\n'))
card_real = 0
card_full = 0
for i in range(1, num):
    card = int(input())
    card_real = card_real + card
for i in range(1, num + 1):
    card_full = card_full + i
print(card_full - card_real)
