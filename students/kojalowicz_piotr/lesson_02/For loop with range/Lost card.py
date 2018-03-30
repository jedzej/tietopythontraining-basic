correctAmount = 0
sumOfCard = 0
numberOfCard = int(input())
for card in range(numberOfCard - 1):
    card = int(input())
    sumOfCard += card
for card in range(numberOfCard + 1):
    correctAmount += card
print(correctAmount - sumOfCard)