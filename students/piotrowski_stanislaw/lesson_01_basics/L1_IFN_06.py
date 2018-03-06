#https://snakify.org/lessons/integer_float_numbers/problems/car_route/
#piotrsta

from math import ceil

print('Podaj mozliwy kilometraz na dzien: ')
kmPerDay = int(input())
print('Podaj dlugosc trasy: ')
route = int(input())

days=ceil(route/kmPerDay)
print('Liczba dni potrzebnych na przebycie tej trasy to: ')
print(days)


