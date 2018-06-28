line_nr = int(input())
city_country = {}

for i in range(line_nr):
    line_str = input()
    line_list = line_str.split(' ')
    country = line_list[0]
    cities = line_list[1:]
    for city in cities:
        city_country.setdefault(city, country)

line_nr = int(input())
for i in range(line_nr):
    country = input()
    print(city_country[country])
