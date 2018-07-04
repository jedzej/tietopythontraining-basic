# There was a set of cards with numbers from 1 to m.
# One of the card is now lost.
# Determine the number on that
# lost card given the numbers for the remaining cards.

print('Give the numbers of cards: ')
m = int(input())

total = 0
for i in range(1, m):
    print('Enter a value: ')
    n = int(input())
    total -= n
for i in range(1, m + 1):
    total += i

print('The lost card = ' + str(int(total)))
