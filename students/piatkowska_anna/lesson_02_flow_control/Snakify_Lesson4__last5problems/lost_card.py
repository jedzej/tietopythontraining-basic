#Statement
#There was a set of cards with numbers from 1 to N. 
#One of the card is now lost. Determine the number on that lost
#card given the numbers for the remaining cards.
#Given a number N, followed by N − 1 integers - 
#representing the numbers on the remaining cards 
#(distinct integers in the range from 1 to N). 
#Find and print the number on the lost card.

def LostCard():
    print("Enter number of cards (N):")
    a = int(input())
    print("Enter "+str(a-1)+" numbers between 1-" + str(a)+ ":" )
    sumInput = 0
    sum = 0
    for j in range(a + 1):
        sum +=j
    for i in range(a - 1):
        print("Card number " + str(i+1)+":")
        sumInput += int(input())
    print("The lost card is:")
    print(sum - sumInput)

if __name__ == '__main__':
    LostCard()