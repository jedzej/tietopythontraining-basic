#https://snakify.org/lessons/integer_float_numbers/problems/car_route/
#piotrsta
import math

print('Podaj mozliwy kilometraz na dzien: ')
km_per_day = int(input())
print('Podaj dlugosc trasy: ')
route = int(input())

days = math.ceil(route / km_per_day)
print('Liczba dni potrzebnych na przebycie tej trasy to: ')
print(days)
