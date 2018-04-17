countries_cities = dict()
for i in range(int(input())):
	country, *cities = (input()).split()
	countries_cities[country] = cities


for j in range(int(input())):
	city = input()
	for country_key in countries_cities.keys():
		if city in countries_cities[country_key]:
			print(country_key)
