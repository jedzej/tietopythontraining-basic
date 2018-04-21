n = int(input())
cify_of_country = {}

for i in range(n):
    country, *cities = input().split()
    cify_of_country[country] = set(cities)

m = int(input())
for i in range(m):
    city = input()
    for country, cities in cify_of_country.items():
        if city in cities:
            print(country)
