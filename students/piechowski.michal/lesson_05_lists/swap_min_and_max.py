#!/usr/bin/env python3

list = [int(x) for x in input().split()]
list_length = len(list)

index_of_maximum = 0
index_of_minimum = 0

for i in range(0, list_length):
    if list[i] < list[index_of_minimum]:
        index_of_minimum = i
    if list[i] > list[index_of_maximum]:
        index_of_maximum = i

maximum = list[index_of_maximum]
minimum = list[index_of_minimum]
list[index_of_maximum] = minimum
list[index_of_minimum] = maximum

for i in range(0, list_length):
    print(list[i], end = ' ')
