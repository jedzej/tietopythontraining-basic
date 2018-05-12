def main():
    city_country_dict = {}
    for x in range(int(input("Number of countries: "))):
        country, *cities = input("#" + str(x + 1) + " Type a country "
                                 "and list of cities: ").split()
        for city in cities:
            city_country_dict[city] = country

    for x in range(int(input("Number of cities: "))):
        print(city_country_dict[input("#" + str(x + 1) + " Type a city: ")])


if __name__ == '__main__':
    main()
