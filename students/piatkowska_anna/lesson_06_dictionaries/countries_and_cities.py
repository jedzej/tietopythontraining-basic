'''
Statement
Given a list of countries and cities of each country.
Then given the names of the cities.
For each city specify the country in which it is located.

'''


def cities():
    n = int(input("Enter number of countries: "))
    country_dict = {}
    for i in range(n):
        country, *cities = input("Enter country name and\
 list of cities separeted by space: ").split()
        values = [country] * len(cities)
        country_dict.update(dict(zip(cities, values)))
    m = int(input("Enter number of cities: "))
    for i in range(m):
        city = input("Enter city: ")
        print(country_dict[city])


if __name__ == "__main__":
    cities()
