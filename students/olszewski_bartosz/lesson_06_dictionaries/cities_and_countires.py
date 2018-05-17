number_of_countries = int(input())
cities = dict()
for city in range(number_of_countries):
    entry = input().split(' ')
    cities[entry[0]] = entry[1:]

number_of_checks = int(input())
for checks in range(number_of_checks):
    city = str(input())
    for key, val in cities.items():
        if city in val:
            print(key)
