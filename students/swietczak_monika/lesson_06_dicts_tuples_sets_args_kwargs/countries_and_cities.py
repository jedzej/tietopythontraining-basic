n = int(input())
cities_dict = {}
for i in range(n):
    country, *cities = input().split()
    for city in cities:
        cities_dict[city] = country
m = int(input())
for _ in range(m):
    print(cities_dict[input()])

# print(cities_dict)
