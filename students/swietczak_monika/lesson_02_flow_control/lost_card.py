
n = int(input("How many cards should be? "))
sum_of_cards = 0

for i in range(1, n + 1):
    sum_of_cards += i
for i in range(n - 1):
    sum_of_cards -= int(input("Enter card number: "))

print(sum_of_cards)
