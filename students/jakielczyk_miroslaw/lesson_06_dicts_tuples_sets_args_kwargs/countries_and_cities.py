n = int(input())
country_and_cities_dict = dict()
for x in range(n):
    country_and_cities = input().split(' ')
    country_and_cities_dict[country_and_cities[0]] = \
        country_and_cities[1:]

number_of_cities = int(input())
for city in range(number_of_cities):
    name_of_city = input()
    for key in country_and_cities_dict:
        if name_of_city in country_and_cities_dict[key]:
            print(key)
