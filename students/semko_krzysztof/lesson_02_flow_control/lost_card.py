"""
There was a set of cards with numbers from 1 to N.
One of the card is now lost.
Determine the number on that lost card given the numbers
for the remaining cards.

Given a number N, followed by N − 1 integers -
representing the numbers on the remaining cards
(distinct integers in the range from 1 to N).
Find and print the number on the lost card.
"""

print("Please input the number of cards:")
cards_number = int(input())

sum_of_cards = 0
input_cards = 0
for i in range(1, cards_number + 1):
    sum_of_cards += i

for i in range(cards_number - 1):
    input_cards += int(input())

# Mocno to uproszczone... Przydałoby się tutaj jakieś sprawdzanie
# już wprowadzonych wartości, ale bez list(wektorów) nie mam pomysłu jak to zrobić

print("Missing card is: " + str(sum_of_cards - input_cards))
