#https://snakify.org/lessons/integer_float_numbers/problems/digit_after_decimal_point/
#piotrsta

import math

print('Podaj dodatnia liczbe rzeczywista: ')
num = float(input())

frac, whole = math.modf(num)
frac2=str(frac)
print('Pierwsza cyfra czesci dziesietnej tej liczby wynosi: ')
print((frac2)[2])


