number_of_countries = int(input())
cities = dict()
ACTION = 0
ACTION_2 = 1
for city in range(number_of_countries):
    entry = input().split(' ')
    cities[entry[ACTION]] = entry[ACTION_2:]

number_of_checks = int(input())
for checks in range(number_of_checks):
    city = str(input())
    for key, val in cities.items():
        if city in val:
            print(key)
