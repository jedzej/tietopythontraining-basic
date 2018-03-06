#https://snakify.org/lessons/integer_float_numbers/problems/fractional_part/
#piotrsta

import math

print('Podaj dodatnia liczbe rzeczywista: ')
num = float(input())

frac, whole = math.modf(num)
print('Czesc dziesietna tej liczby wynosi: ')
print(frac)


