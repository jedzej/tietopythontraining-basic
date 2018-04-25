def main():
    city_country_dict = {}
    for x in range(int(input())):
        country, *cities = input().split()
        for city in cities:
            city_country_dict[city] = country

    for x in range(int(input())):
        print(city_country_dict[input()])


if __name__ == '__main__':
    main()
