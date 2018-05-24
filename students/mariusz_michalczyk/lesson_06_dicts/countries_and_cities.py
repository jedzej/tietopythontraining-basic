def get_countries_and_cities(n):
    storage = {}
    for i in range(n):
        line = [s for s in input().split()]
        country = line[0]
        cities = set(line[1::])
        storage[country] = cities
    return storage


def show_country(m, storage):
    for i in range(m):
        city = input()
        for country, cities in storage.items():
            if city in cities:
                print(country)


if __name__ == '__main__':
    n = int(input())
    storage = get_countries_and_cities(n)
    m = int(input())
    show_country(m, storage)
