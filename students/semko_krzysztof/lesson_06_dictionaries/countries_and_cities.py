"""
Given a list of countries and cities of each country.
Then given the names of the cities. For each city
specify the country in which it is located.
"""


def main():
    database = {}
    countries_count = int(input())
    for i in range(countries_count):
        country, *cities = input().split()
        database[country] = cities

    cities_count = int(input())
    for j in range(cities_count):
        city = input()
        for key in database:
            cities = database[key]
            if city in cities:
                print(key)


if __name__ == '__main__':
    main()
