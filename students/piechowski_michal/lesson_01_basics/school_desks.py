#!/usr/bin/env python3

from math import ceil

numberOfStudentsInFirstClass = int(input())
numberOfStudentsInSecondClass = int(input())
numberOfStudentsInThirdClass = int(input())
desksNeeded = ceil(numberOfStudentsInFirstClass / 2) + ceil(numberOfStudentsInSecondClass / 2) + ceil(numberOfStudentsInThirdClass / 2)
print(desksNeeded)
