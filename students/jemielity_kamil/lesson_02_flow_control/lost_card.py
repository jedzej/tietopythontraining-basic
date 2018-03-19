
n = int(input('Highest number of card: '))
total = 0
maximum = 0
for i in range(1, n):
    number = int(input("Card number: "))
    total += number

for i in range(1, n + 1):
    maximum += i

lost_card = maximum - total
print(lost_card)
