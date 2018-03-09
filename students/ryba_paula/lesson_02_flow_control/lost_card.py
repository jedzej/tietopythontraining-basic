cards = int(input())

sum_of_cards = 0
remaining_cards = 0

for i in range(1, cards + 1):
    sum_of_cards += i

for i in range(1, cards):
    remaining_cards += int(input())
    
print(sum_of_cards - remaining_cards)