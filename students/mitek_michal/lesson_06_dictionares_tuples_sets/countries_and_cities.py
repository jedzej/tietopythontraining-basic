
def countries_and_cities():

    countries = {}

    for i in range(int(input())):

        country, *cities = input().split()

        for city in cities:
            countries[city] = country

    for i in range(int(input())):
        print(countries[input()])


if __name__ == '__main__':
    countries_and_cities()
