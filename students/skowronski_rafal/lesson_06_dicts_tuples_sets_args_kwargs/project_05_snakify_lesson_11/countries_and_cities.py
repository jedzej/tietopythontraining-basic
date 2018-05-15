if __name__ == '__main__':
    countries_and_cities = [input().split() for i in
                            range(int(input('Enter number of countries: ')))]

    cities_and_countries_dict = dict()
    for item in countries_and_cities:
        for city in item[1:]:
            cities_and_countries_dict[city] = item[0]

    cities_array = [input() for i in
                    range(int(input('Enter number of cities: ')))]

    print(end='\n')
    for city in cities_array:
        country = cities_and_countries_dict[city]
        print(country)
