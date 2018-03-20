print("Lost card\n")

N = int(input("Enter the number of cards: "))

x = 0
y = 0

for i in range(1, N):
    n = int(input("Enter the value of the card: "))
    x += n

for i in range(1, N + 1):
    y += i

lost_card = y - x

print("\nThe number on the lost card is: {:d}".format(lost_card))
