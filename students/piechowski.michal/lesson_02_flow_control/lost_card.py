#!/usr/bin/env python3

number_of_cards = int(input())
sum_of_cards = (number_of_cards + 1) * number_of_cards / 2

for i in range(1, number_of_cards):
    sum_of_cards -= int(input())

print(sum_of_cards)
