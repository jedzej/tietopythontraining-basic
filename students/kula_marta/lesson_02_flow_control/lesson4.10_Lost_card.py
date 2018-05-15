#!/usr/bin/env python

import math

cards = int(input())
sum_of_cards = int(math.fsum(range(cards + 1)))

for i in range(cards - 1):
    sum_of_cards -= int(input())

print(sum_of_cards)
