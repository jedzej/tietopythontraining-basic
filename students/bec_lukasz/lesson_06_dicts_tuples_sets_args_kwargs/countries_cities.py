countries = {}
for i in range(int(input())):
    country, *cities = input().split()
    countries[country] = set(cities)

for i in range(int(input())):
    city = input()
    for keys, values in countries.items():
        if city in values:
            print(keys)
