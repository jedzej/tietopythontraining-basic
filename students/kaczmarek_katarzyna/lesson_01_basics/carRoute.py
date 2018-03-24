import math

dayKm = int(input("Kilometers per day: "))
length = int(input("Route (km): "))

print(math.ceil(length / dayKm))
