#!/usr/bin/env python3


def main():
    n = int(input())
    cities_in_country = {}

    for i in range(0, n):
        country, *cities = input().split()
        cities_in_country[country] = set(cities)

    m = int(input())

    for i in range(0, m):
        city = input()
        for country, cities in cities_in_country.items():
            if city in cities:
                print(country)


if __name__ == "__main__":
    main()