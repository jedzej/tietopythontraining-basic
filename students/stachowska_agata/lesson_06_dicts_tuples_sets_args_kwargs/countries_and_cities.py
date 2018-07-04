countries = {}

for i in range(int(input())):
    country, *cities = input().split()
    for n in cities:
        countries[n] = country

for n in range(int(input())):
    city = input()
    print(countries[city])
