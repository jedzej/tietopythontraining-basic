"""There was a set of cards with numbers from 1 to N. One of the card is
now lost. Determine the number on that lost card given the numbers for
the remaining cards.

Given a number N, followed by N − 1 integers - representing the numbers
on the remaining cards (distinct integers in the range from 1 to N).
Find and print the number on the lost card. """

sum = 0
N = int(input())
for x in range(1, N + 1):
    sum += x
for i in range(N - 1):
    sum -= int(input())
print(sum)
