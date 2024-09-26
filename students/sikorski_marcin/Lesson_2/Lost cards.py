numberOfCards = int(input("Enter number of cards: "))
sumOfNumberOfCards = (((1 + numberOfCards)/2) * numberOfCards)

sum = 0
while numberOfCards != 1:
    number = int(input("Type NOT MISSING numbers: "))
    numberOfCards -= 1
    sum += number

print("Number of lost cards: " +str(sumOfNumberOfCards-sum))