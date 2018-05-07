num_of_countries = int(input('Give the number of countries: '))
motherland = dict()
print('Give the country and cities: ')
for _ in range(num_of_countries):
    country, *cities = input().split()
    for city in cities:
        motherland[city] = country
num_of_cities = int(input('Give the number of cities: '))
print('Give cities:')
for _ in range(num_of_cities):
    city = input()
    print(motherland.get(city))
