#!/usr/bin/env python3


countries_and_cities_database = {}


def check_which_country(city):
    country = countries_and_cities_database.get(city)
    if country:
        return(country)
    else:
        return("There's ain't such city in da database")


def get_input_number_of(item_name):
    try:
        number = int(input("Please enter number of {}\n".format(item_name)))
    except ValueError:
        print("Wrong number, try again\n")
        exit
    return number


def main():
    for _ in range(get_input_number_of("countries")):
        country_and_cities = input(
            "Enter country and it's cities seperated with spaces\n").split()
        country = country_and_cities[0]
        cities = country_and_cities[1:]
        countries_and_cities_database.update({c: country for c in cities})

    for _ in range(get_input_number_of("cities")):
        city_name = input("Enter city name\n")
        print(check_which_country(city_name))


if __name__ == "__main__":
    main()
