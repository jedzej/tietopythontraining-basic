n = int(input())
cify_of_country = {}

for _ in range(n):
    country, *cities = input().split()
    city_of_country[country] = set(cities)

m = int(input())
for _ in range(m):
    city = input()
    for country, cities in city_of_country.items():
        if city in cities:
            print(country)
