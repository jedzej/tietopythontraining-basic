#!/usr/bin/env python3

country_cities = {}

lines = int(input())
for i in range(lines):
    country, *country_cities[country] = input().split()

lines = int(input())
for i in range(lines):
    city = input()
    for country in country_cities:
        if city in country_cities[country]:
            print(country, end=" ")
    print()
