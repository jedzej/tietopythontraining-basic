n = int(input())
cards = 0
for i in range(1, n + 1):
    cards += i
for i in range(n - 1):
    cards -= int(input())
print(cards)

