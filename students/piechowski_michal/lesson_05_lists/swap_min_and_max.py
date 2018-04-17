#!/usr/bin/env python3

number_list = [int(x) for x in input().split()]

maximum = max(number_list)
minimum = min(number_list)

index_of_maximum = number_list.index(maximum)
index_of_minimum = number_list.index(minimum)

number_list[index_of_maximum] = minimum
number_list[index_of_minimum] = maximum

for item in number_list:
    print(item, end=' ')
