#!/usr/bin/env python3
"""Countries and cities exercise"""


def main():
    """Main function"""
    countries = {}
    for _ in range(int(input())):
        country, *cities = input().split()
        countries[country] = cities

    for _ in range(int(input())):
        city = input()
        for country in countries:
            if city in countries[country]:
                print(country)


if __name__ == '__main__':
    main()
