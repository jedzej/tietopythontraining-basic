def make_dict():
    countries = {}
    countries_amount = int(input())
    for i in range(countries_amount):
        country_and_city = input().split()
        countries[country_and_city[0]] = country_and_city[1:]
    how_many_cities = int(input())
    for no_city in range(how_many_cities):
        city = input()
        for key, value in countries.items():
            if city in value:
                print(key)


make_dict()
