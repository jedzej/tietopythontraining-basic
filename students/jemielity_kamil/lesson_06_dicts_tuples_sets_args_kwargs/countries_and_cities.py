countries = dict()
for i in range(int(input('How many countries: '))):
    country, *cities = input("Country and cities: ").split(" ")
    countries[country] = cities

for j in range(int(input('Number of cities: '))):
    city = input("City: ")
    for country_key in countries.keys():
        if city in countries[country_key]:
            print(country_key)
