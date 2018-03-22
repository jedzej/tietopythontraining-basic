#!/usr/bin/env python3


def range_filter(item, range_start, range_end):
    return item >= range_start and item <= range_end


list_of_strings = [str(x) for x in input("Input the list: ").split()]
range_start = int(input("Input range start: "))
range_end = int(input("Input range end: "))
list_of_integers = [int(x) for x in list_of_strings
                    if range_filter(int(x), range_start, range_end)]

print("Filtered list:")
for item in list_of_integers:
    print(item, end=' ')
