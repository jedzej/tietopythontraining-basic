# script to find the lost card in a given set of cards

print("enter the number of cards")
number_of_cards = int(input())
card_list = []
for i in range(number_of_cards-1):
    print("enter card " + str(i+1))
    card = int(input())
    card_list.append(card)

for k in range(len(card_list)+1):
    if k+1 not in card_list:
        print(k+1)
