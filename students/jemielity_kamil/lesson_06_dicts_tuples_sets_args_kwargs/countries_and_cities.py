Countries = dict()
for i in range(int(input('How many countries: '))):
    country, *cities = input("Country and cities: ").split(" ")
    Countries[country] = cities

for j in range(int(input('Number of cities: '))):
    city = input("City: ")
    for country_key in Countries.keys():
        if city in Countries[country_key]:
            print(country_key)
