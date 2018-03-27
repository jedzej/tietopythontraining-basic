"""
description:
    There was a set of cards with numbers from 1 to N.
    One of the card is now lost.
    Determine the number on that lost card given the numbers for the remaining cards.

    Given a number N, followed by N − 1 integers
    - representing the numbers on the remaining cards
    (distinct integers in the range from 1 to N).
    Find and print the number on the lost card.
"""

print("""
    Given a number N, followed by N − 1 integers  
    (distinct integers in the range from 1 to N) 
    finds and prints the number lost.
""")

N = int(input("N = "))
sum = 0

for k in range(N+1):
    sum += k

for k in range(1,N):
    nr = int(input("{}-th number is: ".format(k)))
    sum -= nr

print(sum)

