country_dict = {}
for _ in range(int(input())):
    country, *cities = input().split()
    country_dict[country] = ' '.join(cities)

for _ in range(int(input())):
    city = input()
    for country, cities in country_dict.items():
        if city in cities:
            print(country)
