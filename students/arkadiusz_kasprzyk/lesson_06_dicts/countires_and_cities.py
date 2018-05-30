# countries_and_cities.py

N = int(input("Give N: "))
cities_countries = dict()
for n in range(N):
    nn = input("{}: ".format(n + 1)).split()
    country = nn[0]
    for city in nn[1:]:
        cities_countries[city] = country

M = int(input("Give M: "))
cities = []
for m in range(M):
    cities.append(input("{}: ".format(m + 1)))

print("")  # just aesthetics for testing in Snakify

for city in cities:
    print(cities_countries[city])
