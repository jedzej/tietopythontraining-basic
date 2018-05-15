N = int(input())
cards = []
for x in range(N - 1):
    cards.append(int(input()))

origin = list(range(1, N + 1))
cards.sort()

pos = 0
lost_card = 0
for x in cards:
    if (origin[pos] - cards[pos]) != 0:
        lost_card = origin[pos]
        break
    else:
        pos += 1

if lost_card == 0:
    lost_card = origin.pop()

print(lost_card)
