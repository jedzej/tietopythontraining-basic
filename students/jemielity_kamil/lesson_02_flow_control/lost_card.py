n = int(input('Highest number of card: '))
total = 0
max = 0
for i in range(1, n):
    number = int(input("Card number: "))
    total += number

for i in range(1, n+1):
    max += i

lost_card = max - total
print(lost_card)

