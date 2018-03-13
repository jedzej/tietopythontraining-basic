# There was a set of cards with numbers from 1 to N. One of the card is now
# lost. Determine the number on that lost card given the numbers for the
# remaining cards.

print("Enter biggest card (N) and cards u already have: ")
biggest_card = int(input())

sum = 0

for i in range(1, biggest_card + 1):
    sum += i
for j in range(1, biggest_card):
    card = int(input())
    sum -= card

print(sum)
