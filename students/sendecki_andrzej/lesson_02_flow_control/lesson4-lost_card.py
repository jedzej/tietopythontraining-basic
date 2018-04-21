#There was a set of cards with numbers from 1 to N. One of the card is now lost. #Determine the number on that lost card given the numbers for the remaining cards.
#
#Given a number N, followed by N − 1 integers - representing the numbers on the #remaining cards (distinct integers in the range from 1 to N). Find and print the #number on the lost card. 

import sys

print("Enter the number of cards:")
N = int(input())
if N < 1:
    print("Error: no cards given")
    sys.exit()

#overall sum of cards
sum=0
for i in range(1, N+1):
    sum=sum+i;

print(sum)

#remaining sum of cards
rem_sum = 0
print("Enter the cards:")
for i in range(1, N):    
    a = int(input())
    if(a > N):
        print("Error: no such card");
        sys.exit()

    rem_sum = rem_sum + a

print("Lost card:")
lost = sum - rem_sum
print(lost)



