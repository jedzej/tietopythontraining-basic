N = int(input())
countries = dict()
for i in range(N):
    inp = input().split(" ")
    country = inp[0]
    cities = inp[1:]
    countries.setdefault(country, cities)


M = int(input())
for _ in range(M):
    city = input()
    for country, cities in countries.items():
        if city in cities:
            print(country)
