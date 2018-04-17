countries = {}

for i in range(int(input("How many countries with cities? "))):
    country, *cities = input("Type the country and cities").split()
    for city in cities:
        countries[city] = country

for x in range(int(input("How many cities to check? "))):
    print(countries[input("Type the city: ")])
